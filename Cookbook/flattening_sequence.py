# Wonderful recipe from the Python cookbook

# This is used to flatten lists using yield from keyword


import collections

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, collections.Iterable) and not isinstance(x, ignore_types):
            yield from x
        else:
            yield x


items = [
    [1, 2, 3],
    "Subhayan",
    ["Shaayan", "Dimpu"],
    [34, 45, 56]
]

for item in flatten(items):
    print(item)

# Results

# Subhayans-MacBook-Pro:Cookbook subhayanbhattacharya$ python flattening_sequence.py
# flattening_sequence.py:10: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
#   if isinstance(x, collections.Iterable) and not isinstance(x, ignore_types):
# 1
# 2
# 3
# Subhayan
# Shaayan
# Dimpu
# 34
# 45
# 56
