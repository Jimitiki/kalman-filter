from kalman2 import *
import numpy
import math

MAX_TIME = 0.8

def get_estimated_position(states, start, timestamps):
    total_time = 0.0
    X = array([[states[0][0]], [states[0][1]], [states[0][2]], [start[0]], [start[1]], [start[2]]])
    P = diag((0.01, 0.01, 0.01, 0.01))
    for i in range(0, len(states) - 1):
        delta_t = timestamps[i + 1] - timestamps[i]
        total_time += delta_t
        if (total_time > MAX_TIME):
            return [X[0], X[1]]
        (X, P) = get_next_state(X, P, states[i], delta_t)
    return [X[0], X[1]]

def get_next_state(X, P, state, delta_t):
    A = array([[1, 0, delta_t , 0], [0, 1, 0, delta_t], [0, 0, 1, 0], [0, 0, 0, 1]])
    Q = eye(X.shape[0])
    B = eye(X.shape[0])
    U = zeros((X.shape[0],1)) 
    
    Y = array([[state[0]], [state[1]]])
    H = array([[0, 0, 1, 0], [0, 0, 0, 1]])
    R = eye(Y.shape[0])
    
    (X, P, K, IM, IS, LH) = kf_update(X, P, Y, H, R)
    
    (X, P) = kf_predict(X, P, A, Q, B, U)
    
    return (X, P)
