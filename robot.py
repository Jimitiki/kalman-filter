import commands
import socket
import math
import mathutils
from time import sleep

ADDRESS = ("0.0.0.0", 55555)
BASE_TURN_SPEED = 12
BASE_MOVE_SPEED = 6
ROTATE_DELAY = 0.875 / math.pi / 2

def move_to_point(goal_pos, current_position, current_angle, magnitude):
    distance = mathutils.distance(current_position, goal_pos)
    if (distance < 60):
        return True

    diff = (goal_pos[0] - current_position[0], goal_pos[1] - current_position[1])
    goal_angle = math.atan2(diff[1], diff[0])
    angle_diff = mathutils.wrap_angle(goal_angle - current_angle) 
    print(angle_diff)
    angle = angle_diff / (math.pi) + 1
    print(angle)
    left = magnitude * (angle - 0.5)
    right = magnitude * (1.5 - angle)

    print(left, right)

    commands.set_speed(int(left), int(right))
    return False


def get_robot_position():
    location = commands.where_robot()["center"]

    return location
