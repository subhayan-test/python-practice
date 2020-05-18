# This is a better example of couroutines

import inspect

def simple_coroutine2(a):
    print("Couroutine started...")
    print(f"And couroutine got the value {a}")
    b = yield a
    print(f"Subroutine got the value {b}")
    c = yield a + b
    print(f"Subroutine got the value {c}")

try:
    g = simple_coroutine2(10)
    print(g.send(None))
    print(g.send(100))
    print("Finally..")
    g.send(420)
except StopIteration:
    pass
print(inspect.getgeneratorstate(g))
