# Basic example of yield from , Taken from the fluent Python book
import itertools

def chain(*interables):
    for i in interables:
        yield from i

func = chain(["Subhayan", "Shaayan", "Rohan"], [10, 20, 30])

# Bad way of doing this
# for _ in itertools.repeat(None, 10):
#     print(next(func))

# Good way of doing this
for val in func:
    print(val)

# I guess the best way of doing this :
c = itertools.chain(["Subhayan", "Shaayan", "Rohan"], [10, 20, 30])

for _ in itertools.repeat(None, 10):
    print(next(func))
