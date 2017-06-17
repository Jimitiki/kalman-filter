import commands
import robot
import random
import sys
import math

commands.open_connection(("0.0.0.0", 55555))

commands.set_pid_params(10, 4, 2)

states = []

estimate = []

#have robot follow random vectors, updating predicted position along the way
(x, y) = (random.random() * 10, random.random() * 10)
for i in range(0, int(sys.argv[1])):
    motor_speeds = commands.get_speed()
    position = commands.get_robot_position()
    (speed_l, speed_r) = (motor_speeds["speed_a"], motor_speeds["speed_b"])
    #right motor speed, left motor speed, and motor speed diff
    state = [speed_r, speed_l, speed_r - speed_l]
    states.append(state)
    if len(states) > 8:
        states.pop(0)
    #orientation
    theta = math.atan2(position["orientation"][1], position["orientation"][2])
    #pos_x
    x = position["center"][0]
    #pos_y
    y = position["center"][1]

    #estimate = estimate_position(states)

    robot.follow_vector(x, y, (float("inf"), float("inf")), (estimate[0], estimate[1]), estimate[2])
    sleep(0.1)

sleep(1.5)

if len(estimate) == 3:
    print("Estimated position: " + str(estimate[0]) + "," + str(estimate[1]) + ", estimated orientation: " + str(estimate[2]))
    position = commands.get_robot_position()
    (x, y, theta) = (position["center"][0], position["center"][1], math.atan2(position["orientation"][1], position["orientation"][2]))
    print("Actual position: " + str(x) + "," + str(y) + ", actual orientation: " + str(theta))
    print("Error: (" + str(math.fabs(estimate[0] - x)) + ", " + str(math.fabs(estimate[1] - y)) + ", " + str(math.fabs(estimate[2] - theta)) ")")
