import kalman
import numpy
import math

T_MATRIX = numpy.matrix([
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, -1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1]])

def get_estimated_position(states, start, timestamps):
    for i in range(0, len(states) - 2):
        delta_t = timestamps[i + 1] - timestamps[i]
        state = states[i] + start
        start = get_next_state(state, delta_t)
    return start

def get_next_state(state, delta_t):
    delta_t /= 1000
    distance = state[0] + state[1] - state[2] * 75 * delta_t
    input_matrix = numpy.matrix([0, 0, 0, state[2] / (state[0] + state[1]) * delta_t * math.pi, distance * math.cos(state[3]), distance * math.cos(state[3])])
    prediction = kalman.predict(numpy.matrix(state), numpy.matlib.eye(6), T_MATRIX, input_matrix)
    current = [prediction[3], prediction[4], prediction[5]]
    return current
