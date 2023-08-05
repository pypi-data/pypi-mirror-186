from collections import defaultdict
from math import pi
from random import uniform
from typing import Any, Dict, Iterable, Iterator, Optional, Set, Tuple

from vecgl.linalg import (Vec4, get_frustum_mat4, get_rotate_x_mat4,
                          get_rotate_y_mat4, get_rotate_z_mat4,
                          get_translate_mat4, homogenious_vec4_to_vec3,
                          homogenious_vec4_to_xy_vec2, mul_mat4)
from vecgl.model import Model, get_cube_model
from vecgl.rendering import kDefaultEps, render


def _get_random_vec3(a: float = -2.0, b: float = 2.0):
    return tuple(uniform(a, b) for _ in range(3))


def _is_in_cipping_space(p: Vec4, eps: float = kDefaultEps):
    p3 = homogenious_vec4_to_vec3(p)
    return all(-1.0 - eps <= a and a <= 1.0 + eps for a in p3)


def test_render_random_points():
    model = Model()
    n = 256
    for _ in range(n):
        p = _get_random_vec3()
        model.add_point(p)
    rendered = render(model)
    assert len(rendered.points) <= n
    for pt in rendered.points:
        assert _is_in_cipping_space(pt.p)


def test_render_random_lines():
    model = Model()
    n = 256
    for _ in range(n):
        p = _get_random_vec3()
        q = _get_random_vec3()
        model.add_line(p, q)
    rendered = render(model)
    assert len(rendered.points) <= n
    for ln in rendered.lines:
        assert _is_in_cipping_space(ln.p)
        assert _is_in_cipping_space(ln.q)


def _get_random_angle() -> float:
    return uniform(0, 2 * pi)


def get_rotated_and_rendered_cube_model(ax: float, ay: float, az: float):
    cube = get_cube_model()
    view_mat4 = mul_mat4(get_translate_mat4(0.0, 0.0, -3.0),
                         get_rotate_x_mat4(ax), get_rotate_y_mat4(ay),
                         get_rotate_z_mat4(az))
    projection_mat4 = get_frustum_mat4(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)
    cube_in_ndc = cube.transform(mul_mat4(projection_mat4, view_mat4))
    rendered = render(cube_in_ndc)
    return rendered


Graph = Dict[Any, Set[Any]]


def _get_xy_graph(rendered: Model) -> Graph:
    graph: Graph = defaultdict(set)
    for ln in rendered.lines:
        p = homogenious_vec4_to_xy_vec2(ln.p)
        q = homogenious_vec4_to_xy_vec2(ln.q)
        graph[p].add(q)
        graph[q].add(p)
    return graph


def _get_permutations(n: int) -> Iterator[Tuple[int]]:
    if n == 0:
        yield tuple()
        return
    for perm in _get_permutations(n - 1):
        for i in range(n):
            yield perm[:i] + (n - 1, ) + perm[i:]


def _is_isomorph_graph_perm(graph: Graph, nodes: Tuple[Any], idxs: Dict[Any,
                                                                        int],
                            other_graph: Graph, other_nodes: Tuple[Any],
                            other_idxs: Dict[Any, int], perm: Tuple[int]):

    # Check if the permutation respects node degrees.
    for p in nodes:
        i = idxs[p]
        other_i = perm[i]
        other_p = other_nodes[other_i]
        if len(graph[p]) != len(other_graph[other_p]):
            return False

    # Check if the permutation respects node adjacency.
    for p in nodes:
        i = idxs[p]
        other_i = perm[i]
        other_p = other_nodes[other_i]
        for q in graph[p]:
            j = idxs[q]
            other_j = perm[j]
            other_q = other_nodes[other_j]
            if other_q not in other_graph[other_p]:
                return False

    return True


def _is_isomorph_graph(graph: Graph, other_graph: Graph):

    # To be isomorphic, the graphs must have the same number of nodes.
    n = len(graph)
    if len(other_graph) != n:
        return False

    # Naively test all possible permutations.
    nodes = tuple(graph.keys())
    other_nodes = tuple(other_graph.keys())
    idxs = {nodes[i]: i for i in range(n)}
    other_idxs = {other_nodes[i]: i for i in range(n)}
    return any(
        _is_isomorph_graph_perm(graph, nodes, idxs, other_graph, other_nodes,
                                other_idxs, perm)
        for perm in _get_permutations(n))


def _get_graph_from_tuples(tuples: Iterable[Tuple[Any, Any]]) -> Graph:
    graph: Graph = defaultdict(set)
    for p, q in tuples:
        graph[p].add(q)
        graph[q].add(p)
    return graph


def _get_expected_graph_4() -> Graph:
    #
    #   p ----- q
    #   |       |
    #   |       |
    #   s ----- r
    #
    p, q, r, s = 0, 1, 2, 3
    tuples = [(p, q), (q, r), (r, s), (s, p)]
    return _get_graph_from_tuples(tuples)


def _get_expected_graph_6() -> Graph:
    #
    #      t --- u
    #     /       \
    #    /         \
    #   p --------- q
    #    \         /
    #     \       /
    #      s --- r
    #
    p, q, r, s, t, u = 0, 1, 2, 3, 4, 5
    tuples = [(p, q), (q, r), (r, s), (s, p), (p, t), (t, u), (u, q)]
    return _get_graph_from_tuples(tuples)


def _get_expected_graph_7() -> Graph:
    #
    #      t ----- u
    #     /       /|
    #    /       / |
    #   p ----- q  v
    #   |       | /
    #   |       |/
    #   s ----- r
    #
    p, q, r, s, t, u, v = 0, 1, 2, 3, 4, 5, 6
    tuples = [(p, q), (q, r), (r, s), (s, p), (p, t), (t, u), (u, q), (u, v),
              (v, r)]
    return _get_graph_from_tuples(tuples)


def assert_rotated_and_rendered_cube_model(rendered: Model,
                                           msg: Optional[str] = None):
    expected_graphs = [
        _get_expected_graph_4(),
        _get_expected_graph_6(),
        _get_expected_graph_7(),
    ]
    actual_graph = _get_xy_graph(rendered)
    assert any(_is_isomorph_graph(actual_graph, g)
               for g in expected_graphs), msg


def test_render_random_cube_rotation():
    n = 512
    for _ in range(n):
        ax, ay, az = _get_random_angle(), _get_random_angle(
        ), _get_random_angle()
        rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
        msg = f"ax, ay, az = {ax}, {ay}, {az}"
        assert_rotated_and_rendered_cube_model(rendered, msg)
