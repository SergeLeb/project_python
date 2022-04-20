class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('введите значение через пробел ').split()]
        # val = int(input('введите значение и нажмите Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('введите значение и нажмите Enter - '))
                self.my_list.append(val)
                print(f'текущий список - {self.my_list} \n ')
            except:
                print(f'недопустимое значение - строка и булево')
                y_or_n = input(f'попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'вы вышли'
                else:
                    return f'вы вышли'

try_except = Error(1)
print(try_except.my_input())

