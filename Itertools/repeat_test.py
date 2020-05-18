# Sample code to test the use of the repeat function from the itertools method

import itertools

def print_greetings(name):
    print(f"Hello {name}")

for _ in itertools.repeat(None, 10):
    print_greetings("Shaayan")

# repeat(2) would give a never ending range of 2's
for item in map(pow, range(10), itertools.repeat(2)):
    print(item)

names = list(itertools.repeat("Subhayan", 10))
print(names)

names = ["Subhayan", "Shaayan", "Dimpu"]

check = dict(zip(names, itertools.repeat(10)))
print(check)
