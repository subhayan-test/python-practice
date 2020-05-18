class DemoException(Exception):
    """Just a demo exception for handling exceptions"""

def demo_exc_handling():
    print("Couroutine started...")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("Handling the demoexception... continuing")
            else:
                print(f"Couroutine received {x}")
    finally:
        print("Coroutine ending...")


# Below is the console output
#
# In [3]: gen = demo_exc_handling()
#
# In [4]: next(gen)
# Couroutine started...
#
# In [5]: gen.send(100)
# Couroutine received 100
#
# In [6]: gen.send(200)
# Couroutine received 200
#
# In [7]: import inspect
#
# In [8]: inspect.getgeneratorstate(gen)
# Out[8]: 'GEN_SUSPENDED'
#
# In [9]: gen.throw(DemoException)
# Handling the demoexception... continuing
#
# In [10]: inspect.getgeneratorstate(gen)
# Out[10]: 'GEN_SUSPENDED'
#
# In [11]: gen.throw(ZeroDivisionError)
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-11-9a71b35a42ff> in <module>
# ----> 1 gen.throw(ZeroDivisionError)
#
# ~/Desktop/Studies/Codes/Python/Couroutines/generator_exceptions.py in demo_exc_handling()
#       6     while True:
#       7         try:
# ----> 8             x = yield
#       9         except DemoException:
#      10             print("Handling the demoexception... continuing")
#
# ZeroDivisionError:
#
# In [12]: inspect.getgeneratorstate(gen)
# Out[12]: 'GEN_CLOSED'
