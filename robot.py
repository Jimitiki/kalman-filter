import commands
import socket
import math
import mathutils
from time import sleep

ADDRESS = ("0.0.0.0", 55555)
BASE_TURN_SPEED = 12
BASE_MOVE_SPEED = 6
ROTATE_DELAY = 0.875 / math.pi / 2

def follow_vector(vec_x, vec_y, goal_pos):
    normal_vector = mathutils.normalize(vec_x, vec_y)
    where = commands.where_robot()
    position = where["center"]
    distance = mathutils.distance(position, goal_pos)
    if (distance < 60):
        #commands.set_speed(0, 0)
        return True
    orientation = where["orientation"]

    angle = mathutils.signed_angle(normal_vector, orientation)
    magnitude = mathutils.magnitude(vec_x, vec_y)
    angle = angle / (math.pi) + 1
    left = magnitude * (angle - 1)
    right = magnitude * (1 - angle)
    if (angle < 1.5 and angle > 0.5):
        left += magnitude / 2
        right += magnitude / 2
    """if (angle > 1.5 or angle < 0.5):
        if angle > 1.5:
            angle = 3 - angle
        elif angle < 0.5:
            angle = 1 - angle
        left = -magnitude * (angle - 0.5)
        right = -magnitude * (1.5 - angle)
    else:
        left = magnitude * (angle - 0.5)
        right = magnitude * (1.5 - angle)"""

    commands.set_speed(int(left), int(right))
    sleep(0.05)
    return False


def get_robot_position():
    location = commands.where_robot()["center"]

    return location
