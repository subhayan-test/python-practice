# This is basically the couroutine which does the job of priming the couroutine passed


import functools

def couroutine(func):
    @functools.wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
