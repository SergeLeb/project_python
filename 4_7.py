def fact(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1

for el in fact(int(input('Factorial number: '))):
    print(el)
