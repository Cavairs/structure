
def calculate_salary():
    bet_normal = 1880
    days_off = 2000
    day = int(input(" Кол-во отработаных дней: "))
    salary = []
    if day <= 22:
        normal_salary = bet_normal * day
        print(f"Выплата {normal_salary} рублей")
    elif day >= 22 and day < 32:
        the_weekend = (22 * bet_normal) + ((day - 22) * days_off)
        print(f"Выплата {the_weekend} рублей")
    else:
        if day > 31 or day < 0:
            print("Зарплата за месяц от 1 до 31 дня !!!")
            return calculate_salary()


def calculate_salary_director():
    bet_normal = 5000
    days_off = 2000
    day = int(input(" Кол-во отработаных дней: "))
    salary = []
    if day <= 22:
        normal_salary = bet_normal * day
        print(f"Выплата {normal_salary} рублей")
    elif day >= 22 and day < 32:
        the_weekend = (22 * bet_normal) + ((day - 22) * days_off)
        print(f"Выплата {the_weekend} рублей")
    else:
        if day > 31 or day < 0:
            print("Зарплата за месяц от 1 до 31 дня !!!")
            return calculate_salary_director()
