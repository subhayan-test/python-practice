# An example of using the compress function inside itertools
# If you do not understand you can check this link as well:
# https://www.novixys.com/blog/python-itertools-compress-dropwhile-takewhile-groupby/

import itertools
import random

names = ["Subhayan", "Shaayan", "Dimpu", "Poulomi", "Rakesh"]

choices = [random.choice([0, 1]) for _ in itertools.repeat(None, 10)]
print(choices)

for item in itertools.compress(names, choices):
    print(item)
