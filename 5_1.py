print('Введите данные для записи в файл text_1.txt \nДля окончания ввода введите пустую строку! ')
with open('text_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f'{line}\n')
