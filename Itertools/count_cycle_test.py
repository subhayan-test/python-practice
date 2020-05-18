# Basic example of itertools count method and the cycle method

import itertools

counter = itertools.count(start=1, step=5)
for i in range(15):
    print(next(counter))

names = ("Subhayan", "Shaayan", "Dimpu")
cycle = itertools.cycle(names)
for i in range(10):
    print(next(cycle))
