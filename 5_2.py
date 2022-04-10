with open('text_2.txt', 'r', encoding='utf-8') as f_obj:
    useful = [f'{line}. {count.strip()} - {len(count.split())} слов' for line, count in enumerate(f_obj, 1)]
    print(*useful, f'Всего строк - {len(useful)}.', sep='\n')

