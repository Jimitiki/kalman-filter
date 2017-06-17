def get_estimated_position(states, start):
    for i in range(0, len(states) - 1):
        start = get_next_state(states, i, i + 1, start)
    return start
    
def get_next_state(states, index1, index2, current):
    return current
