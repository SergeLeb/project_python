from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        if time > 160:
            print(f"salary - {(time * rate) + (bonus * (time - 160))}") # если выработка (выше нормы), то премия
        else:
            print(f"(salary - {time * rate}") # если выработка стандарт, то без премии
    except ValueError:
        print("введите данные: выработку часов в месяц, часовую ставку в у/е, премию в у/е за час переработки.")

salary()
