import math

SIN_45 = math.sin(math.pi / 4)
COS_45 = math.cos(math.pi / 4)

def normalize(x, y):
    m = magnitude(x, y)
    if m == 0:
        return (0, 0)
    return (x / m, y / m)

def magnitude(x, y):
    return math.sqrt(x * x + y * y)

def slope(p1, p2):
    return (p1[1] - p2[1]) / (p1[0] - p2[0])

def dot_product(u, v):
    return u[0] * v[0] + u[1] * v[1]

def signed_angle(u, v):
    angle = math.acos(dot_product(u, v))
    sign = math.atan2(v[1], v[0]) - math.atan2(u[1], u[0])
    if sign < 0:
        sign += 2 * math.pi
    sign -= math.pi

    if sign < 0:
        angle *= -1
    return angle

def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)

#displaces the given point p1 towards point p2 by magnitude m and returns the resulting point
def move_point_towards_point(p1, p2, m):
    return move_point_along_vector(p1, (p2[0] - p1[0], p2[1] - p1[1]), m)

def move_point_away_from_point(p1, p2, m):
    return move_point_along_vector(p1, (p1[0] - p2[0], p1[1] - p2[1]), m)

#displaces the given point p1 towards point p2 by magnitude m and returns the resulting point
def move_point_along_vector(p, v, m):
    n_vector = normalize(v[0], v[1])
    return (p[0] + n_vector[0] * m, p[1] + n_vector[1] * m)

def orthoganalize_2D(v, ccw):
    return (v[1], -v[0]) if ccw else (-v[1], v[0])

def build_rect_from_line(p1, p2, w):
    vector = (p1[0] - p2[0], p1[1] - p2[1])
    v1 = orthoganalize_2D(vector, True)
    v2 = orthoganalize_2D(vector, False)

    r1 = move_point_along_vector(p1, v1, w / 2)
    r2 = move_point_along_vector(p2, v1, w / 2)
    r3 = move_point_along_vector(p2, v2, w / 2)
    r4 = move_point_along_vector(p1, v2, w / 2)

    return (r1, r2, r3, r4)

def rotate_vector_45(v):
    return (v[0] * COS_45 - v[1] * SIN_45, v[0] * SIN_45 + v[1] * COS_45)

def rotate_vector_180(v):
    return (-v[0], -v[1])

def line_intersect_test(p1, p2, p3, p4):
    if (max(p1[0], p2[0]) < min(p3[0], p4[0])
            or max(p3[0], p4[0]) < min(p1[0], p2[0])
            or max(p1[1], p2[1]) < min(p3[1], p4[1])
            or max(p3[1], p4[1]) < min(p1[1], p2[1])):
        return False
    if (area(p1, p2, p3) > 0 and area(p1, p2, p4) < 0
            or area(p1, p2, p4) > 0 and area(p1, p2, p3) < 0):
        return True
    return False

def area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
