EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time_elapsed):
    """EMPTY DOC STRING"""
    return EXPECTED_BAKE_TIME - time_elapsed

def preparation_time_in_minutes(num_layers):
    """ EMPTY DOC STRING"""
    return num_layers * PREPARATION_TIME

def elapsed_time_in_minutes(num_layers, time_elapsed):
    """ EMPTY DOC STRING"""
    return preparation_time_in_minutes(num_layers) + time_elapsed
