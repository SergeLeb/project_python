import json

with open('my_ex7.json', 'w', encoding='utf_8') as write_f, open('text_7.txt', encoding='utf_8') as f_obj:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    result = [profit, {'average profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                               len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
