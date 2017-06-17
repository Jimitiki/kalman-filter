import commands
import sys
import math
import statistics

commands.open_connection(("0.0.0.0", 55555))

commands.set_pid_params(10, 4, 2)

speed_a = int(sys.argv[1])
speed_b = int(sys.argv[2])

commands.set_speed(speed_a, speed_b)
avg_speed_l = 0
avg_speed_r = 0

l_speeds = []
r_speeds = []

for i in range(0, 300):
    speeds = commands.get_speed()
    speed_l = int(speeds["speed_a"])
    speed_r = int(speeds["speed_b"])
    avg_speed_l += speed_l
    avg_speed_r += speed_r
    l_speeds.append(speed_l)
    r_speeds.append(speed_r)

avg_speed_l /= 300
avg_speed_r /= 300

print(avg_speed_l, statistics.stdev(l_speeds), avg_speed_r, statistics.stdev(r_speeds))

commands.set_speed(0, 0)

commands.close_connection()
