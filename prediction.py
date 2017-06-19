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
    X = array([[states[0]], [states[1]], [states[2]], [start[0]], [start[1]], [start[2]]])
    P = diag((0.01, 0.01, 0.01, 0.01, 0.01, 0.01))
    for i in range(0, len(states) - 1):
        delta_t = timestamps[i + 1] - timestamps[i]
        total_time += delta_t
        if (total_time > MAX_TIME):
            return [X[3], X[4], X[5]]
        state = states[i] + start
        (X, P) = get_next_state(X, P, state, delta_t)
    return [X[3], X[4], X[5]]

def get_next_state(X, P, state, delta_t):
    Q = eye(X.shape[0])
    B = eye(X.shape[0])
    U = zeros((X.shape[0],1)) 
    
    Y = array([[state[0]], [state[1], [states[2]]]])
    H = array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]])
    R = eye(Y.shape[0])
    
    (X, P) = kalman.update(X, P, Y, H, R)
    
    distance = (state[0] + state[1] - state[2]) * 15 * delta_t
    x_dist = distance * math.cos(state[5])
    y_dist = distance * math.sin(state[5])
    rotation_factor = 0
    if state[2] != 0:
        rotation_factor = state[2] / (2 * (state[0] + state[1])) * (math.fabs(state[2]) / 40) * delta_t * math.pi
    input_matrix = [0, 0, 0, x_dist, y_dist, rotation_factor]
    (X, P) = kalman.predict(X, P, T_MATRIX, input_matrix)
    return (X, P)
