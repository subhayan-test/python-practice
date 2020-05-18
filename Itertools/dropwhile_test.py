# Lets try to use dropwhile and see how it goes and whether i can understand
# The exact opposite of this is takewhile

import itertools

numbers = [2, 4, 6, 8, 10, 7 , 3, 18, 20 , 100]

print("DROPWHILE")
# keep dropping numbers until we get an odd value
for num in itertools.dropwhile(lambda x: x%2 == 0, numbers):
    print(num)

print("TAKEWHILE")
# keep keeping numbers until we get an even value
for num in itertools.takewhile(lambda x: x %2 == 0, numbers):
    print(num)
