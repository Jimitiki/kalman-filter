import commands
import robot
import random
import sys
import math
import mathutils
import prediction
from time import sleep

commands.open_connection(("0.0.0.0", 55555))

commands.set_pid_params(10, 4, 2)

states = []
timestamps = []

estimate = []

#have robot follow random vectors, updating predicted position along the way
for i in range(0, int(sys.argv[1])):
    motor_speeds = commands.get_speed()
    positions = commands.where_all()
    timestamp = positions["time"]
    goal = positions["40"]["center"]
    position = positions["robot"]
    (speed_l, speed_r) = (motor_speeds["speed_a"], motor_speeds["speed_b"])
    #right motor speed, left motor speed, and motor speed diff
    state = [speed_r, speed_l, speed_r - speed_l]
    states.append(state)
    timestamps.append(float(timestamp))
    if len(states) > 8:
        states.pop(0)
        timestamps.pop(0)
    #orientation
    theta = math.atan2(position["orientation"][0], position["orientation"][1]) + math.pi
    if (theta < 0):
        theta += math.pi * 2
    #pos_x
    x = position["center"][0]
    #pos_y
    y = position["center"][1]

    estimate = prediction.get_estimated_position(states, [theta, x, y], timestamps)

    #angle_diff = mathutils.signed_angle()

    robot.move_to_point(goal, (x, y), theta, 10)
    sleep(0.11)

sleep(1.5)

if len(estimate) == 3:
    print("Estimated position: " + str(estimate[0]) + "," + str(estimate[1]) + ", estimated orientation: " + str(estimate[2]))
    position = commands.get_robot_position()
    (x, y, theta) = (position["center"][0], position["center"][1], math.atan2(position["orientation"][0], position["orientation"][1]))
    print("Actual position: " + str(x) + "," + str(y) + ", actual orientation: " + str(theta))
    print("Error: (" + str(math.fabs(estimate[0] - x)) + ", " + str(math.fabs(estimate[1] - y)) + ", " + str(math.fabs(estimate[2] - theta)) + ")")
