def max_value(state):
    v = float("-inf")
    if Terminal(state):
        return Utility(state)
    for action in Actions(state):
        v = max(v, min_value(Result(state, action)))
    return v