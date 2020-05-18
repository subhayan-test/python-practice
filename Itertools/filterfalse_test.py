# Test the inner workings of the filterfalse function in python

import itertools

c = itertools.count(start=2, step=3)
values = [next(c) for _ in itertools.repeat(None, 10)]
print(values)

print("Checking example of filterfalse..")
for val in itertools.filterfalse(lambda x: x%2 == 0, values):
    print(val)
