# Simple couroutine which calculates the running average of numbers
# There are two examples presented here one without priming and the other one with priming

from priming_couroutines import couroutine

def calc_average():
    average = 0
    total = 0
    count = 0
    while True:
        value = yield average
        total += value
        count += 1
        average = total/count

@couroutine
def calc_average_with_priming():
    average = 0
    total = 0
    count = 0
    while True:
        value = yield average
        total += value
        count += 1
        average = total/count


# This has to be tried out in the terminal and i copy paste the output here
# The below one is without priming

# In [1]: from average_calculator import calc_average
#
# In [2]: g = calc_average()
#
# In [3]: next(g)
# Out[3]: 0
#
# In [4]: g.send(10)
# Out[4]: 10.0
#
# In [5]: g.send(20)
# Out[5]: 15.0
#
# In [6]: g.send(30)
# Out[6]: 20.0
#
# In [7]: g.close()
#
# In [8]: g
# Out[8]: <generator object calc_average at 0x1121de650>
#
# In [9]: g.send(90)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-9-489a64c83898> in <module>
# ----> 1 g.send(90)
#
# StopIteration:
#
# In [10]: import inspect
#
# In [11]: inspect.getgeneratorstate(g)
# Out[11]: 'GEN_CLOSED'


# This is the screen output of the second example which uses priming

# 
# In [1]: from average_calculator import *
#
# In [2]: gen = calc_average_with_priming()
#
# In [3]: import inspect
#
# In [4]: inspect.getgeneratorstate(gen)
# Out[4]: 'GEN_SUSPENDED'
#
# In [5]: gen.send(10)
# Out[5]: 10.0
#
# In [6]: gen.send(20)
# Out[6]: 15.0
#
# In [7]: gen.send(30)
# Out[7]: 20.0
#
# In [8]: gen.close()
#
# In [9]: inspect.getgeneratorstate(gen)
# Out[9]: 'GEN_CLOSED'
