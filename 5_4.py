rus_dic = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

with open('text_4_new.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])
