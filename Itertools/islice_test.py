# Code to understand the inner workings of the islice itertools function
# There is nothing special about this, works very similar to the built in slice functionality
import itertools

values = list(range(2, 21))
print(values)

for val in itertools.islice(values, 0, None, 3):
    print(val)
