import datetime
from art import *
from application.salary import calculate_salary, calculate_salary_director
from application.db.people import get_employees

date_now = datetime.date.today()


def main():
    while True:
        tprint(f'Сегодня {date_now}')
        print('Зарплата сотрудников')
        print('1 - Инженеры')
        print('2 - Директоры')
        print('3 - Список сотрудников')
        print('4 - Выход')
        a = int(input('Выбирите отдел: '))
        if a == 1:
            print('Расcчитаем зарплату инженеров')
            calculate_salary()
        elif a == 2:
            print('Расcчитаем зарплату директоров')
            calculate_salary_director()
        elif a == 3:
            print('Должность - сотрудник')
            get_employees()
        elif a == 4:
            break
        return main()


if __name__ == "__main__":
    main()
