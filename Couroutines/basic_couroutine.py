# This is the basic example of a couroutine used in the generator function
# All these examples are taken from the fluent Python book
import inspect

def simple_couroutine():
    print("Couroutine started...")
    x = yield
    print(f"The couroutine received {x}")


c = simple_couroutine()
print(inspect.getgeneratorstate(c))
print(c)
print(inspect.getgeneratorstate(c))
next(c)
print(inspect.getgeneratorstate(c))
c.send(420)
print(inspect.getgeneratorstate(c))
