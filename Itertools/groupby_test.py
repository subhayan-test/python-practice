# Code to understand the workings of the groupby function inside itertools module

import itertools


letters = 'BCDDIIJKNNOOPPPSTTVX'

for key, group in itertools.groupby(letters):
    print(key, list(group))
