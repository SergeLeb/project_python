class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'модель устройства ': self.name, 'цена за ед ': self.price, 'количество ': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'введите наименование ')
            unit_p = int(input(f'введите цену за ед '))
            unit_q = int(input(f'введите количество '))
            unique = {f'модель устройства ': unit, 'цена за ед ': unit_p, 'количество ': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'текущий список - \n {self.my_store}')
        except:
            return f'ошибка ввода данных'

        print(f'для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'весь склад - \n {self.my_store_full}')
            return f'выход'
        else:
            return StoreMashines.reception(self)

class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'

class Scaner(StoreMashines):
    def to_scan(self):
       return f'to scan smth {self.numb} times'

class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth {self.numb} times'

unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scaner('Canon', 10000, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
