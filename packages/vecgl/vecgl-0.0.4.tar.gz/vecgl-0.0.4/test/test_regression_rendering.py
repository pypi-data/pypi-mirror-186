from test.test_fuzzing_rendering import (
    assert_rotated_and_rendered_cube_model,
    get_rotated_and_rendered_cube_model)

from vecgl.model import Model
from vecgl.rendering import render


def test_regression_render_cube_rotation_1():
    ax, ay, az = 1.570829848348178, 6.250446710139106, 5.785181940242188
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_2():
    ax, ay, az = 1.5694041560784535, 1.563997545701588, 2.1631326469014285
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_3():
    ax, ay, az = 1.4267271853173198, 4.712695377173559, 1.870277735870633
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_4():
    ax, ay, az = 1.5710363340251863, 4.819605540428241, 4.683413904395169
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_5():
    ax, ay, az = 5.533173210184067, 3.531582766859654, 5.504429586588959
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_6():
    ax, ay, az = 0.35078291488936114, 1.2078982535137388, 1.747348682368665
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 9
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_7():
    ax, ay, az = 1.635127044888502, 0.9221427816819399, 4.661062940774574
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_8():
    ax, ay, az = 1.5729186731731524, 1.5631322304934274, 6.202168063467976
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_9():
    ax, ay, az = 6.124255956325768, 2.6732258212011306, 1.1278723988970296
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 9
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_10():
    ax, ay, az = 1.1990177600729368, 3.528060831944588, 2.633709723220587
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 9
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_11():
    ax, ay, az = 5.895474909909089, 5.689106487389601, 3.0577563018537925
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 9
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_12():
    ax, ay, az = 1.6535555777097155, 4.711946869034812, 1.4584106314305814
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_13():
    ax, ay, az = 4.712489872476942, 5.120227704155422, 3.0095742421136147
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_14():
    ax, ay, az = 2.9167850915952664, 1.2211547625437351, 2.142172344879036
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 12


def test_regression_render_cube_rotation_15():
    ax, ay, az = 2.1308012576023505, 6.269238538765256, 5.480182002329142
    rendered = get_rotated_and_rendered_cube_model(ax, ay, az)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 9
    assert len(rendered.triangles) == 12


def test_regression_render_partial_cube_1():
    model = Model()
    model.add_line(
        (1.3570081004945758, 1.0, 1.4466046399182133, 3.3981570232861698),
        (0.39815702328616975, 1.0, -0.3440183651510318, 1.6429918995054242))
    model.add_triangle(
        (0.39815702328616975, -1.0, -0.3440183651510318, 1.6429918995054242),
        (-1.3570081004945758, 1.0, 0.634203440889867, 2.6018429767138302),
        (0.39815702328616975, 1.0, -0.3440183651510318, 1.6429918995054242))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_regression_render_partial_cube_2():
    model = Model()
    model.add_line(
        (-0.10229209143436296, 0.12573321567891207, 0.5473344862780072),
        (-0.124849585982334, 0.4569802702556819, 0.44305754102415285))
    model.add_triangle(
        (0.17483020049481068, -0.639921643651093, 0.21201123434377056),
        (-0.6533357316296431, 0.26820604480691196, 0.03888374110736784),
        (0.33005026558261974, 0.013932277348052888, -0.5055274176124662))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_regression_render_partial_cube_3():
    model = Model()
    model.add_line((1.36, 1.00, 1.45, 3.40), (0.40, 1.00, -0.34, 1.64))
    model.add_triangle((-0.40, 1.00, 2.42, 4.36), (1.36, 1.00, 1.45, 3.40),
                       (-1.36, 1.00, 0.63, 2.60))
    rendered = render(model)
    assert len(rendered.lines) == 1
    assert len(rendered.triangles) == 1


def test_regression_render_partial_cube_4():
    model = Model()
    model.add_line(
        (-0.5441065404211226, 0.45125248147324276, 0.024837656538431552),
        (-0.4517022873328635, -0.5437321543041853, -0.004661400904259893))
    model.add_line(
        (-0.5441065404211226, 0.45125248147324276, 0.024837656538431552),
        (0.43563473718159534, 0.5566884341088824, 0.02486284735155271))
    model.add_line(
        (-0.4517022873328635, -0.5437321543041853, -0.004661400904259893),
        (0.5570718705308316, -0.43514560921763396, -0.004634694853504611))
    model.add_line(
        (0.43563473718159534, 0.5566884341088824, 0.02486284735155271),
        (0.5570718705308316, -0.43514560921763396, -0.004634694853504611))
    rendered = render(model)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 4
    assert len(rendered.triangles) == 0


def test_regression_render_partial_cube_5():
    model = Model()
    model.add_line(
        (-0.5341138083130935, -0.36745694959061276, 0.2429328789674624),
        (0.2238277456742943, -0.6159918733346115, -0.2088140072442837))
    model.add_line(
        (-0.5341138083130935, -0.36745694959061276, 0.2429328789674624),
        (-0.5089129538850997, 0.40161680338893657, 0.2429529171441074))
    model.add_line(
        (0.2238277456742943, -0.6159918733346115, -0.2088140072442837),
        (0.38894936499537724, -0.3069456170393892, 0.4261700884743477))
    model.add_line(
        (0.2238277456742943, -0.6159918733346115, -0.2088140072442837),
        (0.26364378080755957, 0.6000575372698783, -0.20876390883518592))
    model.add_line(
        (0.38894936499537724, -0.3069456170393892, 0.4261700884743477),
        (0.408191177506189, 0.2808253271151155, 0.4261817925621189))
    model.add_line(
        (-0.5089129538850997, 0.40161680338893657, 0.2429529171441074),
        (0.26364378080755957, 0.6000575372698783, -0.20876390883518592))
    model.add_line(
        (0.26364378080755957, 0.6000575372698783, -0.20876390883518592),
        (0.408191177506189, 0.2808253271151155, 0.4261817925621189))
    model.add_triangle(
        (0.38894936499537724, -0.3069456170393892, 0.4261700884743477),
        (0.26364378080755957, 0.6000575372698783, -0.20876390883518592),
        (0.408191177506189, 0.2808253271151155, 0.4261817925621189))
    rendered = render(model)
    assert_rotated_and_rendered_cube_model(rendered)
    assert len(rendered.lines) == 7
    assert len(rendered.triangles) == 1
