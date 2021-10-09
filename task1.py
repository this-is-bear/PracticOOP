class Soda:

    def __init__(self, add=''):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print('Газировка и {self.add}')
        else:
            print('Это обычная газировка')
s = Soda()
s.show_my_drink

def main():
    choice = None
    while choice != "0":
        print \
        ("""
        Моя добавка

        1 - Табаско
        2 - Сироп
        3 - Лёд
        """)

        choise = input("Ваш выбор:")
        print()

        if choise == "1":
            print("Ваша добавка: табаско.")
        if choise == "2":
            print("Ваша добавка: сироп.")
        if choise == "3":
            print("Ваша добавка: лёд.")
            


        else:
            print("Извините, в меню нет пункта", choice)
main()