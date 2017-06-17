import commands
import mathutils
from time import sleep
import math
import sys

commands.open_connection(("0.0.0.0", 55555))

commands.set_pid_params(10, 4, 2)

speed = int(sys.argv[1])

delays = [2.2, 1.6, 1.0 , 2.8]

avg_speed = 0

for delay in delays:
    p_init = commands.where_robot()["center"]
    if delay == 1.0:
        speed = -speed
    print(speed)
    commands.set_speed(speed, speed)
    sleep(1.5)
    commands.set_speed(0, 0)
    sleep(1)
    p_next = commands.where_robot()["center"]
    diff_magnitude = math.fabs(mathutils.distance(p_init, p_next))
    print(diff_magnitude)
    avg_speed += diff_magnitude / delay

print(str(avg_speed / len(delays)) + " px/s")

commands.close_connection
