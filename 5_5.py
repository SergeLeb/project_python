from random import randint

with open('text_5.txt', mode='w+', encoding='utf-8') as my_file:
    my_file.write(''.join([str(randint(1, 10)) for _ in range(10)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))
    