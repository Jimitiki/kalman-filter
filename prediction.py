import kalman
import numpy

T_MATRIX = numpy.matrix(
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, -1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1])

def get_estimated_position(states, start):
    start = None
    for i in range(0, len(states) - 2):
        state = states[i] + start
        start = get_next_state(state, i, i + 1)
    return start
    
def get_next_state(state, index1, index2):
    input_matrix = []
    prediction = kalman.predict(numpy.matrix(state), numpy.matlib.eye(6), T_MATRIX, numpy.matlib.eye(6), input_matrix)
    current = [prediction[3], prediction[4], prediction[5]]
    return current
