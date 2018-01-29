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
k = o_one(items)
i = o_n(items)
j = o_n_squared(items)
print(k)
print(i)
print(j)
