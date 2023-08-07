from time import time


def time_def(func):
    def wrap(*args, **kwargs):
        started_at = time()
        result = func(*args, **kwargs)
        print("[time_def] Function: {} Time: {}s".format(func.__name__, round(time() - started_at, 2)))
        return result
    return wrap
