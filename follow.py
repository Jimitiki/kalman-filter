from robot import get_robot_position
from commands import get_speed, where_robot
from math import atan2

waypoints = [(0, 0), (0, 1000), (1000, 1000), (1000, 0)]

states = []

while len(waypoints) > 0:
    robot_speed = get_speed()
    diff = robot_speed[1] - robot_speed[0]
    states.append([robot_speed[0], robot_speed[1], diff])
    sensor_position = get_robot_position()
    sensor_orientation = where_robot()['orientation']
    angle = atan2(sensor_orientation[1], sensor_orientation[0])
    (x, y, new_angle) = get_estimated_position(states, [sensor_position[0], sensor_position[1], angle])
    vec_x = waypoints[0][0] - x
    vec_y = waypoints[0][1] - y
    if follow_vector(vec_x, vec_y, (waypoints[0][0], waypoints[0][1]), (x, y), new_angle):
        waypoints.pop(0)
