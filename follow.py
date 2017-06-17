from robot import get_robot_position
from commands import get_speed

waypoints = [(0, 0), (0, 1000), (1000, 1000), (1000, 0)]

states = []

while len(waypoints) > 0:
    robot_speed =  get_speed()
    diff = robot_speed[1] - robot_speed[0]
    states.append()
    sensor_position = get_robot_position()
    sensor_orientation = get_robot_orientation()
    (orientation, x, y) = get_estimated_position(states)
    vec_x = waypoints[0][0] - x
    vec_y = waypoints[0][1] - y
    if follow_vector(vec_x, vec_y, (waypoints[0][0], waypoints[0][1]), (x, y), orientation):
        waypoints.pop(0)
