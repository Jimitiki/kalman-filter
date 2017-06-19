import kalman
import numpy
import math

T_MATRIX = [
                [1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, -1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1]]

MAX_TIME = 0.8

def get_estimated_position(states, start, timestamps):
    total_time = 0.0
    for i in range(0, len(states) - 1):
        delta_t = timestamps[i + 1] - timestamps[i]
        total_time += delta_t
        if (total_time > MAX_TIME):
            return start
        state = states[i] + start
        start = get_next_state(state, delta_t)
    return start

def get_next_state(state, delta_t):
    distance = (state[0] + state[1] - state[2]) * 15 * delta_t
    x_dist = distance * math.cos(state[5])
    y_dist = distance * math.sin(state[5])
    rotation_factor = 0
    if state[2] != 0:
        rotation_factor = state[2] / (2 * (state[0] + state[1])) * (math.fabs(state[2]) / 40) * delta_t * math.pi
    input_matrix = [0, 0, 0, x_dist, y_dist, rotation_factor]
    prediction = kalman.predict(state, numpy.eye(6), T_MATRIX, input_matrix)[0]
    current = [prediction[3], prediction[4], prediction[5]]
    return current
