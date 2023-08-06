import numpy as np

def to_random_state(rs):
    if not isinstance(rs, np.random.RandomState):
        rs = np.random.RandomState(rs)

    return rs