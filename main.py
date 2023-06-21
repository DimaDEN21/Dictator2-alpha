import random
from random import randint

monthdict = ['Year 0; September','Year 0; October',' Year 0; November','Year 0; December',' Year 0; January','Year 0; February','Year 0; March','Year 0; April','Year 0; May','Year 0; June','Year 0; July','Year 0; August']
money = 10000
army = 50
weapons = 10
armor = 10
stability = 0
starting_tax = 20
money_lost = 0
insurrection_points = 0

def enlist_army():
    global army, money
    while True:
        print("Цена 1 солдата: 2000")
        army_enlist = input("Нанять солдат? (Y/N): ")
        if army_enlist.lower() == "y":
            count_army_enlist = input("Сколько солдат вы хотите нанять?: ")
            if not count_army_enlist.isdigit():
                cls()
                print("Ошибка: Введите положительное целое число.")
                continue
            count_army_enlist = int(count_army_enlist)
            if count_army_enlist * 2000 > money:
                cls()
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следующем месяце.")
            else:
                cls()
                money -= count_army_enlist * 2000
                army += count_army_enlist
                print(count_army_enlist,"Солдат успешно наняты.")
            break
        elif army_enlist.lower() == "n":
            cls()
            print("Отмена найма солдат.")
            break
        else:
            cls()
            print("Ошибка: Введите 'Y' или 'N'.")
            continue



def cls():
    print('\n'*100)

def shop():
    global money, armor, weapons
    print("Время закупок!")
    while True:
        cls()
        print("1 - Купить оружие за 1000 каждое")
        print("2 - Купить броню за 1000 каждый")
        print("3 - Купить оружие и броню")
        print("4 - Закончить закупки в этом месяце")
        choice = input("Введите число соответствующее вашему выбору: ")
        if choice == '1':
            cls()
            print(f"У вас {money} денег")
            count_weapons = int(input("Сколько оружия вы хотите купить?: "))
            if count_weapons * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следующем месяце")
                break
            else:
                money -= count_weapons * 1000
                weapons += count_weapons
                cls()
                print(f"Вы купили {count_weapons} оружия")
                break
        elif choice == '2':
            cls()
            print(f"У вас {money} денег")
            count_armor = int(input("Сколько брони вы хотите купить?: "))
            if count_armor * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следующем месяце")
                break
            else:
                money -= count_armor * 1000
                armor += count_armor
                cls()
                print(f"Вы купили {count_armor} брони")
                break
        elif choice == '3':
            cls()
            print(f"У вас {money} денег")
            count_weapons = int(input("Сколько оружия вы хотите купить?: "))
            if count_weapons * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следующем месяце")
                break
            else:
                money -= count_weapons * 1000
                weapons += count_weapons
            count_armor = int(input("Сколько доспехов вы хотите купить?: "))
            if count_armor * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следующем месяце")
                break
            else:
                money -= count_armor * 1000
                armor += count_armor
                cls()
                print(f"Вы купили {count_weapons} оружия")
                print(f"Вы купили {count_armor} брони")
                break
        elif choice == '4':
            cls()
            print("Закупки завершены")
            break


def tax():
    global money, money_lost, starting_tax, insurrection_points

    if starting_tax >= 35:
        if random.random() == 1:
            insurrection_points += 1
            if insurrection_points >= 1:
                print("С людьми что-то не так!")
            elif insurrection_points >= 2:
                print("С людьми что-то не так!!")
            elif insurrection_points >= 3:
                print("С людьми что-то не так!!!")
            elif insurrection_points >= 4:
                response = input("Восстание? Это конец? (y/n): ")
                if response.lower() == "y":
                    exit()
                else:
                    suppress_insurrection()
    else:
        while starting_tax <= 100:
            response = input("Хотите повысить налог на 5%? (y/n): ")
            if response.lower() == "y":
                starting_tax += 5
                if random.randint(0, 10) <= 4:
                    money_lost += 2000 / 100 * starting_tax
                    money -= money_lost
                    print(f"Вы потеряли {money_lost} денег, но повысили налог.")
                    print("Деньги:", money, ";", "Налог", starting_tax, "%")
                    money += 2000 / 100 * starting_tax
                    print("Деньги с налога", 2000 / 100 * starting_tax)
                    print("Деньги:", money, ";", "Налог", starting_tax, "%")
                    break
                else:
                    print("Вы повысили налог и ничего не потеряли.")
                    money += 2000 / 100 * starting_tax
                    print("Деньги с налога", 2000 / 100 * starting_tax)
                    print("Деньги:", money, ";", "Налог", starting_tax, "%")
                    break
            elif response.lower() == "n":
                money += 2000 / 100 * starting_tax
                print("Деньги с налога", 2000 / 100 * starting_tax)
                print("Деньги:", money, ";", "Налог", starting_tax, "%")
                break
            elif response.lower() == "/":
                print("Подсказка: Это может привести к безпорядкам, потере денег и всего, но повысит ежемесячный доход")
                cls()
            elif starting_tax == 100:
                print("Максимальный налог?")
                money += 2000 / 100 * starting_tax
                print("Деньги:", money, ";", "Налог", starting_tax, "%")
                break
            else:
                return

def suppress_insurrection():
    global money, starting_tax, insurrection_points

    print("Вы подавили восстание!")
    soldiers_cost = 50  # Example cost to allocate soldiers
    soldiers_count = money // soldiers_cost

    if soldiers_count > insurrection_points:
        soldiers_count = insurrection_points

    money -= soldiers_count * soldiers_cost
    insurrection_points -= soldiers_count
    starting_tax -= 10

    print(f"Вы потратили {soldiers_count * soldiers_cost} денег на {soldiers_count} солдат.")
    print(f"Налог был снижен на 10%. Новый налог: {starting_tax}%")
    print("Деньги:", money, ";", "Налог", starting_tax, "%")


def options():
    print("Возможные решения:")
    print("Покупка снаряжения", "1")
    print("Повышение налога", "2")
    print("Призвать людей в солдат", "3")
    print("Закрыть", "4")

    while True:
        option = input("Выберите вариант, соответствующий вашему выбору: (/)")
        option = option.lower()

        if option == "/":
            cls()
            print("Возможность увеличить свои шансы на победу")
            option = option.lower()

        elif option == "1":
            cls()
            print("Покупка снаряжения\n")
            shop()
            break
        elif option == "2":
            cls()
            print("Повышение налога\n")
            tax()
            break
        elif option == "3":
            cls()
            print("Призвать людей в солдат\n")
            enlist_army()  # WIP
            break
        elif option == "4":
            cls()
            print("Закрыто")
            return
        else:
            cls()
            print("Неверный выбор. Пожалуйста, введите корректное значение.")





def stat():
    global money, army, weapons, armor, starting_tax
    print("___________________")
    print("Деньги:",money,";","Налог",starting_tax,"%")
    print("Армия:", army)
    print("Оружие:", weapons)
    print("брони:", armor)
    input("Нажмите Enter, чтобы продолжить.")
    cls()

print("____________________________")
print("Управление: (y=да;n=нет; Если в конце текста есть (/) это значит что если нажать на / появитса подсказка)")
print("ПРОЛОГ")
print("У вас есть возможность управлять капиталом, армией и налогами.")
print("Враг будет нападать каждый месяц в течение года.")
print("Цель: удержать свою солдат и капитал в сохранности.")
print("УДАЧИ.")
input("Нажмите Enter, чтобы продолжить.")

cls()

tax()







#for month in monthdict:
#    print(f"Месяц {month}")
#    print("___________________")
#    print("Деньги:", money,";","Налог",starting_tax,"%")
#    print("Армия:", army)
#    print("Оружие:", weapons)
#    print("брони:", armor)







