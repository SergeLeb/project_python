from random import randint
print(a := [randint(0, 20) for _ in range(20)], [i for i in a if a.count(i) == 1], sep='\n')
