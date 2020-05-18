# Basic itertools example to use the accumulate method from itertools
# There has to be a function which takes two input and returns a single value
# Difference between this and reduce is also depicted here
# In reduce only the last in the list that accumulate returns is printed

import itertools
import functools

def add_two_names(name1, name2):
    return f"{name1} {name2}"

names = ["Subhayan", "Shaayan", "Dimpu", "Poulomi"]

check = itertools.accumulate(names, add_two_names)

for result in check:
    print(result)

print("Checking the same results using reduce function in Python..")

reduced = functools.reduce(add_two_names, names)
print(reduced)
