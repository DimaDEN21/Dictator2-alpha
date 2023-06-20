import random
import os
import platform
from random import randint

monthdict = ['Year 0; September','Year 0; October',' Year 0; November','Year 0; December',' Year 0; January','Year 0; February','Year 0; March','Year 0; April','Year 0; May','Year 0; June','Year 0; July','Year 0; August']
money = 10000
army = 50
weapons = 10
armor = 10
stability = 0
starting_tax = 20

#def enlist_army():  #WIP

def cls():
    print('\n'*100)

def shop():
    print("Время закупок!")
    while True:
        print("1 - Купить оружие за 1000 каждое")
        print("2 - Купить брони за 1000 каждый")
        print("3 - Купить оружие и броню")
        print("4 - Закончить закупки в этом месяце")
        choice = int(input("Введите число соответствующее вашему выбору: "))
        if choice == 1:
            count_weapons = int(input("Сколько оружия вы хотите купить?: "))
            if count_weapons * 1000 > money:
                    print("Вам отказано.")
                    print("Недостаточно средств.")
                    print("Попробуйте в следуйщем месяце")
            else:
                money -= count_weapons * 1000
                weapons += count_weapons
        elif choice == 2:
            count_armor = int(input("Сколько брони вы хотите купить?: "))
            if count_armor * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следуйщем месяце")
            else:
                money -= count_armor * 1000
                armor += count_armor
        elif choice == 3:
            count_weapons = int(input("Сколько оружия вы хотите купить?: "))
            if count_weapons * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следуйщем месяце")
            else:
                money -= count_weapons * 1000
                weapons += count_weapons
            count_armor = int(input("Сколько доспехов вы хотите купить?: "))
            if count_armor * 1000 > money:
                print("Вам отказано.")
                print("Недостаточно средств.")
                print("Попробуйте в следуйщем месяце")
            else:
                money -= count_armor * 1000
                armor += count_armor
        elif choice == 4:
            break

def tax():
    starting_tax = 20
    money_lost = 0
    money = 10000
    if starting_tax >= 35:
        if random()==1:
            # Люди просят снизить налог на 10 если нет то С людьми что то не так!
            insurrection_points += 1
            if insurrection_points >= 1:
                print("С людьми что то не так!")
            elif insurrection_points >= 2:
                print("С людьми что то не так!!")
            elif insurrection_points >= 3:
                print("С людьми что то не так!!!")
            elif insurrection_points >= 4:
                input("Востание? Это конец?")
                #возможность подавить востание с помощью расходов на армию и саму армию на фарш + снизить налог
                exit()
    else:
        while (starting_tax<=100):
            response = input("Хотите повысить налог на 5%?: (/)")
            if response.lower() == "y":
                starting_tax += 5
                if random.randint(0,10) <= 4:
                    money_lost += 2000/100 * starting_tax  #25% а не просто 25
                    money -= money_lost
                    print(f"Вы потеряли {money_lost} денег но повысили налог.")
                    print("Деньги:", money,";","Налог",starting_tax,"%")
                    money += 2000/100 * starting_tax
                    print("Деньги с налога",2000/100 * starting_tax)
                    print("Деньги:", money, ";", "Налог", starting_tax, "%")
                    break
                else:
                    print("Вы повысили налог и ничего не потеряли.")
                    money += 2000/100 * starting_tax
                    print("Деньги с налога", 2000 / 100 * starting_tax)
                    print("Деньги:", money, ";", "Налог", starting_tax, "%")
                    break
            elif response.lower() == "n":
                money += 2000/100 * starting_tax
                print("Деньги с налога", 2000/100 * starting_tax)
                print("Деньги:", money,";","Налог",starting_tax,"%")
                break
            elif response.lower() == "/":
                print("Подсказака:","Это может привести к безпорядкам потере денег и всего но повисит ежемесечный доход")
                cls()
            elif starting_tax==100:
                print("Максимальный налог?")
                money += 2000/100 * starting_tax
                print("Деньги:", money, ";", "Налог", starting_tax, "%")
                break
            else:
                return


def options():
    print("Возможные решения:")
    print("Покупка снарежения","1")
    print("Повышение налога", "2")
    print("Призвать людей в армию", "3")
    print("Ничего", "4")
    option = input("Выберите вариант соответствующий вашему выбору:")
    while option != 1 or 2 or 3 or 4 or "/":
        return
    else:
        if option == "/":
            print("Возможность увеливеть свои шансы на победу")
        elif option == 1:
            print("Покупка снарежения")
            shop()
        elif option == 2:
            print("Повышение налога")
            tax()
        elif option == 3:
            print("Призвать людей в армию")
            enlist_army()  #WIP
        elif option == 4:
            print("Ничего")

def stat():
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
print("Цель: удержать свою армию и капитал в сохранности.")
print("УДАЧИ.")
input("Нажмите Enter, чтобы продолжить.")
cls()

stat()

tax()





#for month in monthdict:
#    print(f"Месяц {month}")
#    print("___________________")
#    print("Деньги:", money,";","Налог",starting_tax,"%")
#    print("Армия:", army)
#    print("Оружие:", weapons)
#    print("брони:", armor)







