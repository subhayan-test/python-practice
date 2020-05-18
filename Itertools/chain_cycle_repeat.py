# Example of using itertools chain, repeat and cycle all together

import itertools


fruits = ['apples', 'oranges', 'bananas', 'pineapples','grapes',"berries"]

check = itertools.chain(itertools.repeat(10, 2), itertools.cycle(range(1, 3)))

for _ in itertools.repeat(None, 10):
    print(next(check))

# # for item in zip(fruits, check):
# #     print(item)
#
# check = dict(zip(fruits, check))
# print(check)
