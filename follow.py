from robot import get_robot_position, move_to_point
from commands import get_speed, where_robot, where_markers, where_all
from prediction import get_estimated_position
from math import atan2
from time import sleep
import commands

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = where_markers()
waypoints = []

for marker_number in markers:
    if (marker_number == "time" or marker_number == "robot"):
        continue
    waypoints.append(markers[marker_number]["center"])

states = []
timestamps = []

while len(waypoints) > 0:
    robot_speed = get_speed()
    diff = robot_speed['speed_b'] - robot_speed['speed_a']
    states.append([robot_speed['speed_a'], robot_speed['speed_b'], diff])
    timestamps.append(float(where_all()['time']))
    if len(states) > 3:
        states.pop(0)
        timestamps.pop(0)
    sensor_position = get_robot_position()
    sensor_orientation = where_robot()['orientation']
    angle = atan2(sensor_orientation[1], sensor_orientation[0])
    (x, y, new_angle) = get_estimated_position(states, [sensor_position[0], sensor_position[1], angle], timestamps)
    if move_to_point((waypoints[0][0], waypoints[0][1]), (x, y), new_angle, 12):
        waypoints.pop(0)
    sleep(.1) #the follow_vector also sleeps for 0.05 seconds

commands.set_speed(0, 0)
