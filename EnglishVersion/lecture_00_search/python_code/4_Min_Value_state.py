def min_value(state):
    v = float("inf")
    if Terminal(state):
        return Utility(state)
    for action in Actions(state):
        v = min(v, max_value(Result(state, action)))
    return v