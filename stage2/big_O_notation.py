def o_one(items):
    return 1 
#1 operation so O(1)
def o_n(items):
    total = 0
    # Walks through all items once so O(n)
    for item in items:
        total += item
    return total

def o_n_squared(items):
    total = 0 
    # Walks through all items n*n times so O(n**2)
    for a in items:
        for b in items:
            total += a * b

    return total

n = 10
items = range(n)
one_one = o_one(items)
one_n = o_n(items)
one_n_squared = o_n_squared(items)
print(one_one)
print(one_n)
print(one_n_squared)
