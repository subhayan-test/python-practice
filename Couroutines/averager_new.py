from typing import NamedTuple

class Result(NamedTuple):
    count: int
    average: float

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        count += 1
        total += term
        average = total/count
    return Result(count=count, average=average)
