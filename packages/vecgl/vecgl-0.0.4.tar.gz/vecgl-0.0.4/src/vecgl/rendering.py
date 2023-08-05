from typing import Iterable, Iterator, List, Tuple

from vecgl.bb3tree import BB3Tree, BoundingBox3, create_bb3tree
from vecgl.linalg import (Vec3, add_vec3, cross_vec3, dot_vec3,
                          homogenious_vec4_to_vec3, is_finite_vec3,
                          kDefaultEps, max_vec3, min_vec3, norm2_vec3,
                          ortho_vec2, right_of_vec2, scale_vec3, sub_vec2,
                          sub_vec3, vec3_to_homogenious_vec4, vec3_to_xy_vec2,
                          xy_vec2_to_vec3, z_vec3)
from vecgl.model import Line, Model, Point, Triangle

Plane3 = Tuple[Vec3, Vec3]


def _get_clipping_space_planes() -> Iterator[Plane3]:

    # Collect the 6 boundary planes.
    # Ensure that normals point towards the clipping space.
    for i in range(3):
        for a in [-1.0, 1.0]:
            u = [0.0, 0.0, 0.0]
            u[i] = a
            p = tuple(u)
            u[i] = -a
            n = tuple(u)
            pl = p, n
            yield pl


def _get_triangle_front_plane(tr: Triangle) -> Plane3:
    p, q, r = tr.p, tr.q, tr.r

    # Do this in non-homogenious coordinates.
    p, q, r = homogenious_vec4_to_vec3(p), homogenious_vec4_to_vec3(
        q), homogenious_vec4_to_vec3(r)

    # Compute normal and ensure that it points away from the covered volume.
    pq = sub_vec3(q, p)
    pr = sub_vec3(r, p)
    n = cross_vec3(pq, pr)
    if z_vec3(n) > 0.0:
        n = scale_vec3(-1.0, n)

    # Return the front boundary plane of the triangle.
    return p, n


def _get_triangle_side_planes(tr: Triangle) -> Iterator[Plane3]:
    p, q, r = tr.p, tr.q, tr.r

    # Do this in non-homogenious coordinates.
    p, q, r = homogenious_vec4_to_vec3(p), homogenious_vec4_to_vec3(
        q), homogenious_vec4_to_vec3(r)

    # Project to the xy-plane to compute the normals.
    p2 = vec3_to_xy_vec2(p)
    q2 = vec3_to_xy_vec2(q)
    r2 = vec3_to_xy_vec2(r)

    # Find out if the triangle is in counter-clockwise order and the normals are
    # to the right.
    pq2 = sub_vec2(q2, p2)
    pr2 = sub_vec2(r2, p2)
    normals_to_the_right = right_of_vec2(pq2, pr2)

    # Collect the three boundary planes per side of the triangle.
    n_pq2 = ortho_vec2(pq2, normals_to_the_right)
    n_pq = xy_vec2_to_vec3(n_pq2, 0.0)
    yield p, n_pq
    qr2 = sub_vec2(r2, q2)
    n_qr2 = ortho_vec2(qr2, normals_to_the_right)
    n_qr = xy_vec2_to_vec3(n_qr2, 0.0)
    yield q, n_qr
    rp2 = sub_vec2(p2, r2)
    n_rp2 = ortho_vec2(rp2, normals_to_the_right)
    n_rp = xy_vec2_to_vec3(n_rp2, 0.0)
    yield r, n_rp


def _get_relevant_triangles_query(bb: BoundingBox3) -> BoundingBox3:

    # Relevant triangle are all those that
    #   (i)  intersect the bounding box, or
    #   (ii) the clipping space in front of it.
    lb_x, lb_y, _ = bb.lb
    query_lb = lb_x, lb_y, -1.0
    query_ub = bb.ub
    return BoundingBox3(query_lb, query_ub)


def _get_point_bbox(pt: Point) -> BoundingBox3:

    # Do this in non-homogenious coordinates.
    p = homogenious_vec4_to_vec3(pt.p)

    return BoundingBox3(p, p)


def _get_line_bbox(ln: Line) -> BoundingBox3:

    # Do this in non-homogenious coordinates.
    p, q = homogenious_vec4_to_vec3(ln.p), homogenious_vec4_to_vec3(ln.q)

    lb = min_vec3(p, q)
    ub = max_vec3(p, q)
    return BoundingBox3(lb, ub)


def _get_triangle_bbox(tr: Triangle) -> BoundingBox3:

    # Do this in non-homogenious coordinates.
    p, q, r = homogenious_vec4_to_vec3(tr.p), homogenious_vec4_to_vec3(
        tr.q), homogenious_vec4_to_vec3(tr.r)

    lb = min_vec3(p, q, r)
    ub = max_vec3(p, q, r)
    return BoundingBox3(lb, ub)


def _is_point_visible_wrt_plane(pl: Plane3, q: Vec3,
                                is_visible_on_plane: bool) -> bool:
    if not is_finite_vec3(q):
        return False
    p, n = pl
    if not is_finite_vec3(p, n):
        return True
    pq = sub_vec3(q, p)
    threshold = -kDefaultEps if is_visible_on_plane else kDefaultEps
    return dot_vec3(pq, n) > threshold


def _is_point_visible_wrt_clipping_space(pt: Point) -> bool:

    # Do this in non-homogenious coordinates.
    p = homogenious_vec4_to_vec3(pt.p)

    # For a point to be visible, it must be on or within all clipping space
    # boundary planes.
    for boundary_pl in _get_clipping_space_planes():
        if not _is_point_visible_wrt_plane(
                boundary_pl, p, is_visible_on_plane=True):
            return False
    return True


def _is_point_visible_wrt_triangle(pt: Point, tr: Triangle) -> bool:

    # Do this in non-homogenious coordinates.
    p = homogenious_vec4_to_vec3(pt.p)

    # For a point to be visible, it must be
    #   (i)  on or in front of the triangle plane, or
    #   (ii) outside any of the three remaining boundary planes.
    front_pl = _get_triangle_front_plane(tr)
    if _is_point_visible_wrt_plane(front_pl, p, is_visible_on_plane=True):
        return True
    for boundary_pl in _get_triangle_side_planes(tr):
        if _is_point_visible_wrt_plane(boundary_pl,
                                       p,
                                       is_visible_on_plane=False):
            return True

    return False


def _get_visible_points(points: Iterable[Point],
                        triangle_tree: BB3Tree) -> Iterable[Point]:
    for pt in points:

        # Points must be
        #   (i)  in clipping space, and
        #   (ii) not covered by any triangle.
        if not _is_point_visible_wrt_clipping_space(pt):
            continue
        query = _get_relevant_triangles_query(_get_point_bbox(pt))
        rel_triangles = triangle_tree.find(query)
        if all(_is_point_visible_wrt_triangle(pt, tr) for tr in rel_triangles):
            yield pt


def _get_visible_line_fraction_wrt_plane(
        pl: Plane3, q: Vec3, r: Vec3,
        is_visible_on_plane: bool) -> Tuple[bool, float]:
    if not is_finite_vec3(q, r):
        return True, 0.0

    # If both end points are visible, so is the line between them.
    if _is_point_visible_wrt_plane(
            pl, q, is_visible_on_plane) and _is_point_visible_wrt_plane(
                pl, r, is_visible_on_plane):
        return True, 1.0

    # Find the intersection, if any.
    p, n = pl
    if not is_finite_vec3(p, n):
        return True, 1.0
    qr = sub_vec3(r, q)
    denom = dot_vec3(qr, n)
    if abs(denom) < kDefaultEps:
        return True, 0.0
    qp = sub_vec3(p, q)
    intersection = dot_vec3(qp, n) / denom
    intersection = min(max(intersection, 0.0), 1.0)

    # Return the visible fraction.
    is_front = dot_vec3(n, qr) < 0
    return is_front, intersection


def _get_line_fragment_from_fractions(ln: Line, fraction_start: float,
                                      fraction_end: float,
                                      inverted: bool) -> Iterator[Line]:
    assert 0.0 <= fraction_start and fraction_start <= 1.0
    assert 0.0 <= fraction_end and fraction_end <= 1.0

    # Do this in non-homogenious coordinates.
    p, q = homogenious_vec4_to_vec3(ln.p), homogenious_vec4_to_vec3(ln.q)

    if not is_finite_vec3(p, q):
        return

    # If the fraction is empty, yield nothing or the full line segment.
    pq = sub_vec3(q, p)
    pq_length = norm2_vec3(pq)
    if (fraction_end - fraction_start) * pq_length < kDefaultEps:
        if inverted:
            yield ln
        return

    # Find the end points of the visible line fragment(s). Use the original
    # homogenious line points if possible to avoid numeric inconsistencies.
    p_fraction_start = ln.p
    if fraction_start * pq_length > kDefaultEps:
        p_fraction_start = vec3_to_homogenious_vec4(
            add_vec3(p, scale_vec3(fraction_start, pq)))
    q_fraction_end = ln.q
    if fraction_end * pq_length < pq_length - kDefaultEps:
        q_fraction_end = vec3_to_homogenious_vec4(
            add_vec3(p, scale_vec3(fraction_end, pq)))

    # Yield the line fragments as requested.
    if inverted and ln.p != p_fraction_start:
        yield Line(ln.p, p_fraction_start, ln.color)
    if not inverted:
        yield Line(p_fraction_start, q_fraction_end, ln.color)
    if inverted and q_fraction_end != ln.q:
        yield Line(q_fraction_end, ln.q, ln.color)


def _get_visible_line_fragment_wrt_clipping_space(ln: Line) -> Iterator[Line]:

    # Do this in non-homogenious coordinates.
    p, q = homogenious_vec4_to_vec3(ln.p), homogenious_vec4_to_vec3(ln.q)

    # There will be at most one visible line fragment within the clipping space.
    # For a line fragment to be visible, it must be on or within all clipping
    # space boundary planes. We start with a fully visible line as an over
    # approximation.
    fraction_start = 0.0
    fraction_end = 1.0
    for boundary_pl in _get_clipping_space_planes():
        is_front, fraction = _get_visible_line_fraction_wrt_plane(
            boundary_pl, p, q, is_visible_on_plane=True)
        if is_front:
            fraction_end = min(fraction_end, fraction)
        else:
            fraction_start = max(fraction_start, fraction)

    yield from _get_line_fragment_from_fractions(ln,
                                                 fraction_start,
                                                 fraction_end,
                                                 inverted=False)


def _get_visible_line_fragments_wrt_triangle(ln: Line,
                                             tr: Triangle) -> Iterator[Line]:

    # Do this in non-homogenious coordinates.
    p, q = homogenious_vec4_to_vec3(ln.p), homogenious_vec4_to_vec3(ln.q)

    # There will be at most two visible line fragments that are not covered by
    # the triangle:
    #   (i)  a head fragment starting in p, and
    #   (ii) a tail fragment ending in q.
    # For a line fragment to be visible, it must be
    #   (i)  on or in front of the triangle plane, or
    #   (ii) outside any of the three remaining boundary planes.
    # We start with empty head and tail fragments as an under approximation.
    head_fraction_end = 0.0
    tail_fraction_start = 1.0

    # Analyse visibility wrt. the triangle plane.
    front_pl = _get_triangle_front_plane(tr)
    is_front, faction = _get_visible_line_fraction_wrt_plane(
        front_pl, p, q, is_visible_on_plane=True)
    if is_front:
        head_fraction_end = max(head_fraction_end, faction)
    else:
        tail_fraction_start = min(tail_fraction_start, faction)

    # Analyse visibility wrt. the remaining boundary planes.
    for boundary_pl in _get_triangle_side_planes(tr):
        is_front, fraction = _get_visible_line_fraction_wrt_plane(
            boundary_pl, p, q, is_visible_on_plane=False)
        if is_front:
            head_fraction_end = max(head_fraction_end, fraction)
        else:
            tail_fraction_start = min(tail_fraction_start, fraction)

    yield from _get_line_fragment_from_fractions(ln,
                                                 head_fraction_end,
                                                 tail_fraction_start,
                                                 inverted=True)


def _get_visible_line_fragments(lines: List[Line],
                                triangle_tree: BB3Tree) -> Iterable[Line]:

    # Visible line fragments must be
    #   (i)  in clipping space, and
    #   (ii) not covered by any triangle.
    for ln in lines:
        for ln_root_fragment in _get_visible_line_fragment_wrt_clipping_space(
                ln):
            query = _get_relevant_triangles_query(
                _get_line_bbox(ln_root_fragment))
            rel_triangles = triangle_tree.find(query)
            ln_fragment_list = [ln_root_fragment]
            for tr in rel_triangles:
                ln_fragment_list_next: List[Line] = []
                for ln_fragment in ln_fragment_list:
                    ln_fragment_list_next.extend(
                        _get_visible_line_fragments_wrt_triangle(
                            ln_fragment, tr))
                ln_fragment_list = ln_fragment_list_next
            for ln_fragment in ln_fragment_list:
                yield ln_fragment


def render(model: Model) -> Model:
    rendered = Model()
    triangle_tree = create_bb3tree(model.triangles, _get_triangle_bbox)
    rendered.points = list(_get_visible_points(model.points, triangle_tree))
    rendered.lines = list(
        _get_visible_line_fragments(model.lines, triangle_tree))
    rendered.triangles = model.triangles  # Not yet implemented.
    rendered.rendered = True
    return rendered
