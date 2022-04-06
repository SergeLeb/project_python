from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))
