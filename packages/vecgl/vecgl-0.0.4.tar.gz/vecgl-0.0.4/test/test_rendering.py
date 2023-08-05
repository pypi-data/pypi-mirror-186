from vecgl.linalg import (get_frustum_mat4, get_rotate_y_mat4,
                          get_translate_mat4, mul_mat4)
from vecgl.model import Model, get_cube_model
from vecgl.rendering import render


def test_render_points_outside_of_clipping_space():
    model = Model()
    model.add_point((1.25, 0.0, 0.0))
    model.add_point((0.0, 1.0, 0.0))
    model.add_point((0.0, 1.0, 0.5))
    rendered = render(model)
    assert len(rendered.points) == 2


def test_render_point_on_clipping_space_edge():
    model = Model()
    model.add_point((-1.0, 1.0, -1.0))
    rendered = render(model)
    assert len(rendered.points) == 1


def test_render_point_behind_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.25, 0.25, 1.0))
    rendered = render(model)
    assert len(rendered.points) == 0
    assert len(rendered.triangles) == 1


def test_render_point_ifo_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.25, 0.25, -1.0))
    rendered = render(model)
    assert len(rendered.points) == 1
    assert len(rendered.triangles) == 1


def test_render_point_next_to_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((-0.5, 0.5, 0.0))
    rendered = render(model)
    assert len(rendered.points) == 1
    assert len(rendered.triangles) == 1


def test_render_point_on_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.2, 0.2, 0.0))
    rendered = render(model)
    assert len(rendered.points) == 1
    assert len(rendered.triangles) == 1


def test_render_point_on_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.5, 0.5, 0.0))
    rendered = render(model)
    assert len(rendered.points) == 1
    assert len(rendered.triangles) == 1


def test_render_point_behind_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.5, 0.5, 1.0))
    rendered = render(model)
    assert len(rendered.points) == 0
    assert len(rendered.triangles) == 1


def test_render_point_ifo_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_point((0.5, 0.5, -1.0))
    rendered = render(model)
    assert len(rendered.points) == 1
    assert len(rendered.triangles) == 1


def test_render_line_outside_of_clipping_space():
    model = Model()
    model.add_line((-2.3, 0.0, 0.0), (4.5, 0.0, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 1


def test_render_lines_outside_of_clipping_space():
    model = Model()
    model.add_line((-1.0, -1.0, 1.0), (1.0, 1.0, 0.5))
    model.add_line((0.0, 0.0, 0.0), (0.3, 0.4, 0.5))
    model.add_line((-2.3, 0.0, 0.0), (4.5, 0.0, 0.0))
    model.add_line((-2.3, -0.1, 0.4), (4.5, 0.2, -0.3))
    model.add_line((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
    model.add_line((2.0, 2.0, -2.0), (2.0, 2.0, 2.0))
    rendered = render(model)
    assert len(rendered.lines) == 5


def test_render_line_behind_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    model.add_line((-1.0, -1.0, 1.0), (1.0, 1.0, 0.5))
    rendered = render(model)
    assert len(rendered.lines) == 2
    assert len(rendered.triangles) == 1


def test_render_line_ifo_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((-1.0, -1.0, -0.5), (1.0, 1.0, -1.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_next_to_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((-1.0, 0.0, 0.0), (0.0, -1.0, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_on_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((0.0, 0.0, 0.0), (0.5, 0.5, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_on_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_behind_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((1.0, 0.0, 0.5), (0.0, 1.0, 0.25))
    rendered = render(model)
    assert len(rendered.lines) == 0
    assert len(rendered.triangles) == 1


def test_render_line_ifo_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((1.0, 0.0, -0.25), (0.0, 1.0, -0.5))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_partly_behind_triangle_edge():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((1.0, 0.0, -1.0), (0.0, 1.0, 1.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1
    ln = rendered.lines[0]
    assert (1.0, 0.0, -1.0, 1.0) == ln.p
    assert (0.5, 0.5, 0.0, 1.0) == ln.q


def test_render_line_through_triangle_cw():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    model.add_line((-0.5, -0.5, 1.0), (1.0, 1.0, -1.0))
    rendered = render(model)
    assert len(rendered.lines) == 2
    assert len(rendered.triangles) == 1


def test_render_line_through_triangle_ccw():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    model.add_line((1.0, 1.0, -1.0), (-0.5, -0.5, 1.0))
    rendered = render(model)
    assert len(rendered.lines) == 2
    assert len(rendered.triangles) == 1


def test_render_very_shallow_line_through_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    model.add_line((0.1, 0.9, 0.1), (0.9, 0.1, -0.1))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_very_shallow_line_behind_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    model.add_line((0.1, 0.9, 0.1), (0.9, 0.1, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 0
    assert len(rendered.triangles) == 1


def test_render_very_shallow_line_ifo_triangle():
    model = Model()
    model.add_triangle((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0))
    model.add_line((0.1, 0.9, -0.1), (0.9, 0.1, 0.0))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_render_line_on_clipping_space_edge():
    model = Model()
    model.add_line((-1.0, 1.0, -1.0), (-1.0, 0.0, 1.0))
    rendered = render(model)
    assert len(rendered.lines) == 1


def test_render_line_in_focal_point():
    model = Model()
    model.add_line((0.0, 0.0, 0.0), (0.0, 1.0, 0.0))
    projection_mat4 = get_frustum_mat4(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)
    cube_in_ndc = model.transform(projection_mat4)
    rendered = render(cube_in_ndc)
    assert len(rendered.lines) == 0


def test_render_point_in_focal_point():
    model = Model()
    model.add_point((0.0, 0.0, 0.0))
    projection_mat4 = get_frustum_mat4(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)
    cube_in_ndc = model.transform(projection_mat4)
    rendered = render(cube_in_ndc)
    assert len(rendered.points) == 0


def test_render_cube():
    cube = get_cube_model()
    view_mat4 = mul_mat4(get_translate_mat4(0.0, 0.0, -3.0),
                         get_rotate_y_mat4(0.5))
    projection_mat4 = get_frustum_mat4(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)
    cube_in_ndc = cube.transform(mul_mat4(projection_mat4, view_mat4))
    rendered = render(cube_in_ndc)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_render_cube_from_front():
    cube = get_cube_model()
    view_mat4 = get_translate_mat4(0.0, 0.0, -3.0)
    projection_mat4 = get_frustum_mat4(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)
    cube_in_ndc = cube.transform(mul_mat4(projection_mat4, view_mat4))
    rendered = render(cube_in_ndc)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_rendering_empty_line():
    model = Model()
    model.add_line((-0.09, 0.23, 0.56), (-0.09, 0.23, 0.56))
    model.add_triangle((0.243, -0.609, -0.207), (-0.523, 0.384, 0.242),
                       (0.243, 0.609, -0.207))
    rendered = render(model)
    assert len(rendered.lines) == 0
