from functools import reduce
from math import acos, copysign, cos, inf, isfinite, sin, sqrt
from operator import add, sub
from typing import Callable, List, Tuple, Union

Vec2 = Tuple[float, float]
Vec3 = Tuple[float, float, float]
Vec4 = Tuple[float, float, float, float]
Mat2 = Tuple[Vec2, Vec2]
Mat3 = Tuple[Vec3, Vec3, Vec3]
Mat4 = Tuple[Vec4, Vec4, Vec4, Vec4]

kDefaultEps = 0.00000001

# 2D cartesian coordinates.


def x_vec2(u: Vec2) -> float:
    ux, _ = u
    return ux


def y_vec2(u: Vec2) -> float:
    _, uy = u
    return uy


def str_vec2(u: Vec2) -> str:
    ux, uy = u
    return f"({ux:.2f}, {uy:.2f})"


def _cwise_unary_vec2(fn: Callable[[float], float], u: Vec2):
    ux, uy = u
    return fn(ux), fn(uy)


def _cwise_binary_vec2(fn: Callable[[float, float], float], u: Vec2, v: Vec2):
    ux, uy = u
    vx, vy = v
    return fn(ux, vx), fn(uy, vy)


def _cwise_nary_vec2(fn: Callable[[float, float], float], *us: Vec2) -> Vec2:
    return reduce(lambda u, v: _cwise_binary_vec2(fn, u, v), us)


def _is_finite_vec2(u: Vec2) -> bool:
    ux, uy = u
    return isfinite(ux) and isfinite(uy)


def is_finite_vec2(*us: Vec2) -> bool:
    return all(_is_finite_vec2(u) for u in us)


def uniform_vec2(a: float) -> Vec2:
    return a, a


def is_eps_eq_vec2(u: Vec2, v: Vec2, eps: float = kDefaultEps):
    ux, uy = u
    vx, vy = v
    return abs(ux - vx) < eps and abs(uy - vy) < eps


def is_null_vec2(u: Vec2, eps: float = kDefaultEps) -> bool:
    return is_eps_eq_vec2(u, uniform_vec2(0), eps)


def scale_vec2(a: float, u: Vec2) -> Vec2:
    return _cwise_unary_vec2(lambda ui: a * ui, u)


def add_vec2(*us: Vec2) -> Vec2:
    return _cwise_nary_vec2(add, *us)


def sub_vec2(*us: Vec2) -> Vec2:
    return _cwise_nary_vec2(sub, *us)


def dot_vec2(u: Vec2, v: Vec2) -> float:
    ux, uy = u
    vx, vy = v
    return ux * vx + uy * vy


def min_vec2(*us: Vec2) -> Vec2:
    return _cwise_nary_vec2(min, *us)


def max_vec2(*us: Vec2) -> Vec2:
    return _cwise_nary_vec2(max, *us)


def mean_vec2(*us: Vec2) -> Vec2:
    return scale_vec2(1.0 / len(us), add_vec2(*us))


def norm2_vec2(u: Vec2) -> float:
    return sqrt(dot_vec2(u, u))


def norm1_vec2(u: Vec2) -> float:
    ux, uy = u
    return abs(ux) + abs(uy)


def angle_vec2(u: Vec2, v: Vec2) -> float:
    return acos(dot_vec2(u, v) / (norm2_vec2(u) * norm2_vec2(v)))


def unit_vec2(u: Vec2) -> Vec2:
    return scale_vec2(1.0 / norm2_vec2(u), u)


def right_ortho_vec2(u: Vec2) -> Vec2:
    ux, uy = u
    return uy, -ux


def left_ortho_vec2(u: Vec2) -> Vec2:
    ux, uy = u
    return -uy, ux


def ortho_vec2(u: Vec2, right: bool) -> Vec2:
    return right_ortho_vec2(u) if right else left_ortho_vec2(u)


def right_of_vec2(u: Vec2, v: Vec2) -> bool:
    return dot_vec2(u, right_ortho_vec2(v)) > 0


def left_of_vec2(u: Vec2, v: Vec2) -> bool:
    return dot_vec2(u, left_ortho_vec2(v)) > 0


# 3D cartesian coordinates.


def x_vec3(u: Vec3) -> float:
    ux, _, _ = u
    return ux


def y_vec3(u: Vec3) -> float:
    _, uy, _ = u
    return uy


def z_vec3(u: Vec3) -> float:
    _, _, uz = u
    return uz


def str_vec3(u: Vec3) -> str:
    ux, uy, uz = u
    return f"({ux:.2f}, {uy:.2f}, {uz:.2f})"


def _cwise_unary_vec3(fn: Callable[[float], float], u: Vec3):
    ux, uy, uz = u
    return fn(ux), fn(uy), fn(uz)


def _cwise_binary_vec3(fn: Callable[[float, float], float], u: Vec3, v: Vec3):
    ux, uy, uz = u
    vx, vy, vz = v
    return fn(ux, vx), fn(uy, vy), fn(uz, vz)


def _cwise_nary_vec3(fn: Callable[[float, float], float], *us: Vec3) -> Vec3:
    return reduce(lambda u, v: _cwise_binary_vec3(fn, u, v), us)


def _is_finite_vec3(u: Vec3) -> bool:
    ux, uy, uz = u
    return isfinite(ux) and isfinite(uy) and isfinite(uz)


def is_finite_vec3(*us: Vec3) -> bool:
    return all(_is_finite_vec3(u) for u in us)


def uniform_vec3(a: float) -> Vec3:
    return a, a, a


def is_eps_eq_vec3(u: Vec3, v: Vec3, eps: float = kDefaultEps):
    ux, uy, uz = u
    vx, vy, vz = v
    return abs(ux - vx) <= eps and abs(uy - vy) <= eps and abs(uz - vz) <= eps


def is_null_vec3(u: Vec3, eps: float = kDefaultEps) -> bool:
    return is_eps_eq_vec3(u, uniform_vec3(0.0), eps)


def scale_vec3(a: float, u: Vec3) -> Vec3:
    return _cwise_unary_vec3(lambda ui: a * ui, u)


def add_vec3(*us: Vec3) -> Vec3:
    return _cwise_nary_vec3(add, *us)


def sub_vec3(*us: Vec3) -> Vec3:
    return _cwise_nary_vec3(sub, *us)


def dot_vec3(u: Vec3, v: Vec3) -> float:
    ux, uy, uz = u
    vx, vy, vz = v
    return ux * vx + uy * vy + uz * vz


def cross_vec3(u: Vec3, v: Vec3) -> Vec3:
    ux, uy, uz = u
    vx, vy, vz = v
    return uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx


def min_vec3(*us: Vec3) -> Vec3:
    return _cwise_nary_vec3(min, *us)


def max_vec3(*us: Vec3) -> Vec3:
    return _cwise_nary_vec3(max, *us)


def mean_vec3(*us: Vec3) -> Vec3:
    return scale_vec3(1.0 / len(us), add_vec3(*us))


def norm2_vec3(u: Vec3) -> float:
    return sqrt(dot_vec3(u, u))


def norm1_vec3(u: Vec3) -> float:
    ux, uy, uz = u
    return abs(ux) + abs(uy) + abs(uz)


def angle_vec3(u: Vec3, v: Vec3) -> float:
    return acos(dot_vec3(u, v) / (norm2_vec3(u) * norm2_vec3(v)))


def unit_vec3(u: Vec3) -> Vec3:
    return scale_vec3(1.0 / norm2_vec3(u), u)


# Homogenious coordinates.


def x_vec4(u: Vec4) -> float:
    ux, _, _, _ = u
    return ux


def y_vec4(u: Vec4) -> float:
    _, uy, _, _ = u
    return uy


def z_vec4(u: Vec4) -> float:
    _, _, uz, _ = u
    return uz


def w_vec4(u: Vec4) -> float:
    _, _, _, uw = u
    return uw


def str_vec4(u: Vec4) -> str:
    ux, uy, uz, uw = u
    return f"({ux:.2f}, {uy:.2f}, {uz:.2f}, {uw:.2f})"


def _is_finite_vec4(u: Vec4) -> bool:
    ux, uy, uz, uw = u
    return isfinite(ux) and isfinite(uy) and isfinite(uz) and isfinite(uw)


def is_finite_vec4(*us: Vec4) -> bool:
    return all(_is_finite_vec4(u) for u in us)


def dot_vec4(u: Vec4, v: Vec4) -> float:
    ux, uy, uz, uw = u
    vx, vy, vz, vw = v
    return ux * vx + uy * vy + uz * vz + uw * vw


def mul_mat4_vec4(U: Mat4, v: Vec4) -> Vec4:
    return tuple([dot_vec4(u, v) for u in U])


def _mul_mat4(U: Mat4, V: Mat4) -> Mat4:
    l = len(U)
    m = len(V)
    n = len(V[0])
    W: List[Tuple[float, float, float, float]] = []
    for i in range(l):
        Wi: List[float] = []
        for j in range(n):
            Wij = sum([U[i][k] * V[k][j] for k in range(m)])
            Wi.append(Wij)
        W.append(tuple(Wi))
    return tuple(W)


def mul_mat4(*Us: Mat4) -> Mat4:
    return reduce(_mul_mat4, Us)


def get_unit_mat4() -> Mat4:
    return (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_scale_mat4(ax: float, ay: float, az: float) -> Mat4:
    return (
        (ax, 0.0, 0.0, 0.0),
        (0.0, ay, 0.0, 0.0),
        (0.0, 0.0, az, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_translate_mat4(dx: float, dy: float, dz: float) -> Mat4:
    return (
        (1.0, 0.0, 0.0, dx),
        (0.0, 1.0, 0.0, dy),
        (0.0, 0.0, 1.0, dz),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_rotate_x_mat4(da: float) -> Mat4:
    return (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, cos(da), sin(da), 0.0),
        (0.0, -sin(da), cos(da), 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_rotate_y_mat4(da: float) -> Mat4:
    return (
        (cos(da), 0.0, -sin(da), 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (sin(da), 0.0, cos(da), 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_rotate_z_mat4(da: float) -> Mat4:
    return (
        (cos(da), -sin(da), 0.0, 0.0),
        (sin(da), cos(da), 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_ortho_mat4(l: float, r: float, b: float, t: float, n: float,
                   f: float) -> Mat4:
    return (
        (2.0 / (r - l), 0.0, 0.0, -(r + l) / (r - l)),
        (0.0, 2.0 / (t - b), 0.0, -(t + b) / (t - b)),
        (0.0, 0.0, -2.0 / (f - n), -(f + n) / (f - n)),
        (0.0, 0.0, 0.0, 1.0),
    )


def get_frustum_mat4(l: float, r: float, b: float, t: float, n: float,
                     f: float) -> Mat4:
    return (
        (2.0 * n / (r - l), 0.0, (r + l) / (r - l), 0.0),
        (0.0, 2.0 * n / (t - b), (t + b) / (t - b), 0.0),
        (0.0, 0.0, -(f + n) / (f - n), -2.0 * f * n / (f - n)),
        (0.0, 0.0, -1.0, 0.0),
    )


def get_viewport_mat4(x: float, y: float, w: float, h: float) -> Mat4:
    return (
        (w / 2.0, 0.0, 0.0, x + w / 2.0),
        (0.0, h / 2.0, 0.0, y + h / 2.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    )


# Conversions.


def xy_vec2_to_vec3(u: Vec2, z: float = 0.0) -> Vec3:
    ux, uy = u
    return ux, uy, z


def vec3_to_xy_vec2(u: Vec3) -> Vec2:
    ux, uy, _ = u
    return ux, uy


def homogenious_vec4_to_vec3(u: Union[Vec3, Vec4]) -> Vec3:
    if len(u) == 3:
        return u
    ux, uy, uz, uw = u
    if uw == 0.0:
        return copysign(inf, ux), copysign(inf, uy), copysign(inf, uz)
    return ux / uw, uy / uw, uz / uw


def vec3_to_homogenious_vec4(u: Union[Vec3, Vec4]) -> Vec4:
    if len(u) == 4:
        return u
    ux, uy, uz = u
    return ux, uy, uz, 1.0


def homogenious_vec4_to_xy_vec2(u: Vec4) -> Vec2:
    ux, uy, _, uw = u
    if uw == 0.0:
        return copysign(inf, ux), copysign(inf, uy)
    return ux / uw, uy / uw


def xy_vec2_to_homogenious_vec4(u: Vec2) -> Vec4:
    ux, uy = u
    return ux, uy, 0.0, 1.0
