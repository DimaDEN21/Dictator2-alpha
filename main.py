import random
import time
import os

monthdict = ['Year 0; September', 'Year 0; October', ' Year 0; November', 'Year 0; December', ' Year 0; January',
             'Year 0; February', 'Year 0; March', 'Year 0; April', 'Year 0; May', 'Year 0; June', 'Year 0; July',
             'Year 0; August']
money = 10000
soldier = 30
men_power = 0

armor_level = 5
armor_level_user = 0
soldier_attack_power = 2 * soldier  # сделать 2 изменяемым через улчушения
soldier_defense_power = armor_level * soldier

weapons = 5
armor = 5
starting_tax = 20
money_lost = 0
insurrection_points = 0

soldier_AI = 20
men_power_AI = 0
soldier_attack_power_AI = 4 * soldier_AI  # сделать 4 изменяемым через улчушения
soldier_defense_power_AI = 5 * soldier_AI  # сделать 5 изменяемым через улчушения
weapons_AI = 0
armor_AI = 0


def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0)  # было  0.02

cls = lambda: os.system('cls')


class Main:
    def options_call():
        opt_call = str
        print_slowly("\nНажмите Enter, чтобы продолжить (/ для вызова решений)")
        opt_call = input(".\n")

        if opt_call == "/":
            cls()
            Main.options()
        else:
            cls()
    def options():
        print_slowly("""Возможные решения:
Покупка снаряжения 1
Повышение налога 2
Призвать людей в солдат 3   
Закрыть 4""")

        while True:
            print_slowly("\nВыберите вариант, соответствующий вашему выбору: (/")
            option = input(")")
            option = option.lower()

            if option == "/":
                cls()
                print_slowly("Возможность увеличить свои шансы на победу\n")
                option = option.lower()
                optins_add()
            elif option == "1":
                cls()
                print_slowly("Покупка снаряжения\n")
                Economic.shop()
                break
            elif option == "2":
                cls()
                print_slowly("Повышение налога\n")
                tax()
                break
            elif option == "3":
                cls()
                print_slowly("Призвать людей в солдат\n")
                enlist_soldier()
                break
            elif option == "4":
                cls()
                print_slowly("Решения закрыты\n")
                break
            else:
                cls()
                print_slowly("Неверный выбор. Пожалуйста, введите корректное значение.\n")
                Main.options()

    def stat():
        global money, soldier, weapons, armor, starting_tax, armor_level_user
        print_slowly(f"""___________________
Деньги:{money}; Налог {starting_tax}%
Людской ресурс:{men_power}
Солдаты:{soldier}
Оружие:{weapons}
Брони:{armor}, Уровень брони {armor_level_user}
___________________""")

        Main.options_call()


class Economic:
    def shop():
        global money, armor, weapons
        while True:
            cls()
            print_slowly("Время закупок!\n")
            print_slowly("1 - Купить оружие за 1000 каждое\n")
            print_slowly("2 - Купить броню за 1000 каждый\n")
            print_slowly("3 - Купить оружие и броню\n")
            print_slowly("4 - Закончить закупки в этом месяце\n")
            print_slowly("Введите число соответствующее вашему выбору")
            choice = input(":")

            if choice == '1':
                cls()
                print_slowly(f"У вас {money} денег\n")
                print_slowly("Сколько оружия вы хотите купить?")
                count_weapons = 0
                while True:
                    count_weapons = input(":")
                    if count_weapons.isdigit():
                        count_weapons = int(count_weapons)
                        break
                    else:
                        print_slowly("Введите правильное число\n")
                        print_slowly(input("Нажмите Enter, чтобы попробовать снова"))

                if count_weapons * 1000 > money:
                    print_slowly("Вам отказано.\n")
                    print_slowly("Недостаточно средств.\n")
                    print_slowly(input("Нажмите Enter, чтобы попробовать снова "))
                    continue
                else:
                    money -= count_weapons * 1000
                    weapons += count_weapons
                    cls()
                    print_slowly(f"Вы купили {count_weapons} оружия\n")
                    print_slowly(f"У вас осталось {money} денег")
                    break

            elif choice == '2':
                cls()
                print_slowly(f"У вас {money} денег\n")
                print_slowly("Сколько брони вы хотите купить?")
                count_armor = 0
                while True:
                    count_armor = input(":")
                    if count_armor.isdigit():
                        count_armor = int(count_armor)
                        break
                    else:
                        print_slowly("Введите правильное число\n")
                        print_slowly(input("Нажмите Enter, чтобы попробовать снова"))

                if count_armor * 1000 > money:
                    print_slowly("Вам отказано.\n")
                    print_slowly("Недостаточно средств.\n")
                    print_slowly(input("Нажмите Enter, чтобы попробовать снова"))
                    continue
                else:
                    money -= count_armor * 1000
                    armor += count_armor
                    cls()
                    print_slowly(f"Вы купили {count_armor} брони\n")
                    print_slowly(f"У вас осталось {money} денег")
                    break

            elif choice == '3':
                cls()
                print_slowly(f"У вас {money} денег\n")
                print_slowly("Сколько оружия вы хотите купить?")
                count_weapons = 0
                while True:
                    count_weapons = input(":")
                    if count_weapons.isdigit():
                        count_weapons = int(count_weapons)
                        break
                    else:
                        print_slowly("Введите правильное число\n")
                        print_slowly(input("Нажмите Enter, чтобы попробовать снова"))

                if count_weapons * 1000 > money:
                    print_slowly("Вам отказано.\n")
                    print_slowly("Недостаточно средств.\n")
                    print_slowly(input("Нажмите Enter, чтобы попробовать снова"))
                    continue

                print_slowly("Сколько брони вы хотите купить?")
                while True:
                    count_armor = input(":")
                    if count_armor.isdigit():
                        count_armor = int(count_armor)
                        break
                    else:
                        print_slowly("Введите правильное число\n")
                        print_slowly(input("Нажмите Enter, чтобы попробовать снова"))

                if count_armor * 1000 > money:
                    print_slowly("Вам отказано.\n")
                    print_slowly("Недостаточно средств.\n")
                    print_slowly(input("Нажмите Enter, чтобы попробовать снова"))
                    continue

                money -= count_weapons * 1000
                weapons += count_weapons
                money -= count_armor * 1000
                armor += count_armor
                cls()
                print_slowly(f"Вы купили {count_weapons} оружия\n")
                print_slowly(f"Вы купили {count_armor} брони\n")
                print_slowly(f"У вас осталось {money} денег\n")
                break

            elif choice == '4':
                cls()
                print_slowly("Закупки отменены")
                break

    def suppress_insurrection():
        global money, starting_tax, soldier

        print_slowly("____________________________\n")
        print_slowly("Вы согласились на условия народа!\n")
        soldiers_cost = 100

        money -= soldiers_cost * soldier
        starting_tax -= 10

        print_slowly(f"Вы потратили {soldiers_cost * soldier} денег на {soldier} солдат.\n")
        print_slowly(f"Налог был снижен на 10%. Новый налог: {starting_tax}%\n")
        print_slowly(f"Деньги: {money} ; Налог {starting_tax} %\n")

    def tax():
        global money, money_lost, starting_tax, insurrection_points
        if starting_tax >= 35:
            if random.randint(0, 1) == 1:
                insurrection_points += 1
                if insurrection_points == 1:
                    print_slowly("С людьми что-то не так!")
                elif insurrection_points == 2:
                    print_slowly("С людьми что-то не так!!")
                elif insurrection_points == 3:
                    print_slowly("С людьми что-то не так!!!")
                elif insurrection_points >= 4:
                    print_slowly("""Восстание? Это конец?
Требование людей снизить налоги (y/n)""")
                    response = input(":")
                    if response.lower() == "y":
                        Main.suppress_insurrection()
                    else:
                        exit()
        else:
            while starting_tax <= 100:
                cls()
                print_slowly("Хотите повысить налог на 5%? (y/n) (/)")
                response = input(":")
                if response.lower() == "y":
                    starting_tax += 5
                    if random.randint(0, 10) <= 4:
                        money_lost += 5000 / 100 * starting_tax
                        money -= money_lost
                        print_slowly(f"Вы потеряли {money_lost} денег, но повысили налог.")
                        print_slowly(f"\nДеньги: {money} ; Налог {starting_tax}, %")
                        money += 5000 / 100 * starting_tax
                        print_slowly(f"\nДеньги с налога {5000 / 100 * starting_tax}")
                        print_slowly(f"\nДеньги: {money} ; Налог {starting_tax}, %")
                        break
                    else:
                        print_slowly("Вы повысили налог и ничего не потеряли.")
                        money += 5000 / 100 * starting_tax
                        print_slowly(f"Деньги с налога {5000 / 100 * starting_tax}")
                        print_slowly(f"\nДеньги: {money} ; Налог {starting_tax}, %")
                        break
                elif response.lower() == "n":
                    money += 5000 / 100 * starting_tax
                    print_slowly(f"Деньги с налога {5000 / 100 * starting_tax}")
                    print_slowly(f"\nДеньги: {money} ; Налог {starting_tax}, %")
                    break
                elif response.lower() == "/":
                    print_slowly("Подсказка: Это может привести к безпорядкам, потере денег и всего, но повысит ежемесячный доход\n")
                elif starting_tax == 100:
                    print_slowly("Максимальный налог?")
                    money += 5000 / 100 * starting_tax
                    print_slowly(f"Деньги с налога {5000 / 100 * starting_tax}")
                    print_slowly(f"\nДеньги: {money} ; Налог {starting_tax}, %")
                    break
                else:
                    return

class War_power:
    def training_soldier_stat():
        print_slowly(f"""___________________
Деньги: {money}
Людской ресурс: {men_power}")
Солдаты:{soldier}")
Оружие: {weapons}")
Броня: {armor}, Уровень брони {armor_level_user}")
___________________\n""")

    def training_soldier():
        global men_power, soldier, armor, weapons, money

        while men_power == 0 or soldier == 0 or armor == 0 or weapons == 0 or money == 0:
            print_slowly("Один или более из необходимых требований отсутствует\n")
            Training_soldier.training_soldier_stat()
            print_slowly("Нажмите Enter, чтобы продолжить")
            input(".\n")
            break

        Training_soldier.training_soldier_stat()
        print_slowly("Цена обучения 1 солдата: 1 Оружие, 1 Броня, 1 Людской ресурс\n")

        while True:
            print_slowly("Вы хотите обучить солдат? (Y/N")
            choice = input(")")

            if choice.lower() == "y":
                cls()
                Training_soldier.training_soldier_stat()
                print_slowly("Цена обучения 1 солдата: 1 Оружие, 1 Броня, 1 Людской ресурс\n")

                while True:
                    print_slowly("Сколько солдат вы хотите обучить?")
                    amount_soldier_str = input(":")
                    try:
                        amount_soldier = int(amount_soldier_str)
                        if amount_soldier > int(weapons) or amount_soldier > int(armor) or amount_soldier > int(
                                men_power):
                            cls()
                            Training_soldier.training_soldier_stat()
                            print_slowly(f"Требуется больше ресурсов для обучения {amount_soldier} солдат.\n")
                            continue
                        else:
                            cls()
                            print_slowly(f"Вы обучили {amount_soldier} солдат\n")
                            weapons -= amount_soldier
                            armor -= amount_soldier
                            men_power -= amount_soldier
                            soldier += amount_soldier
                            Training_soldier.training_soldier_stat()
                            break
                    except ValueError:
                        cls()
                        print_slowly("Ошибка: Введите целое число.\n")
            elif choice.lower() == "n":
                exit(0)
            else:
                cls()
                print("Ошибка: Введите 'Y' или 'N'.")
                continue

    def enlist_men_power():
        global men_power, money
        while True:
            print_slowly("Цена призыва 1 людского ресурса: 2000")
            print_slowly("\nНанять солдат? (Y/N)")
            men_power_enlist = input(":")
            if men_power_enlist.lower() == "y":
                print_slowly("\nСколько людей вы хотите призвать?")
                count_men_power_enlist = input(":")
                if not count_men_power_enlist.isdigit():
                    cls()
                    print_slowly("Ошибка: Введите положительное целое число.\n")
                    continue
                count_men_power_enlist = int(count_men_power_enlist)
                if count_men_power_enlist * 2000 > money:
                    cls()
                    print_slowly("Вам отказано.\n")
                    print_slowly("Недостаточно средств.\n")
                    print_slowly("Попробуйте в следующем месяце.\n")
                else:
                    cls()
                    money -= count_men_power_enlist * 2000
                    men_power += count_men_power_enlist
                    print(count_men_power_enlist)
                    print_slowly("Людей успешно призваны.")
                break
            elif men_power_enlist.lower() == "n":
                cls()
                print_slowly("Отмена призыва людей.")
                break
            else:
                cls()
                print_slowly("Ошибка: Введите 'Y' или 'N'.")
                continue

    def armor_upgrade():
        global money, armor_level, armor_level_user
        armor_upgrade_price = armor_level * 2000
        while True:
            print_slowly("Вы хотите улучшить Броню? (Y/N")
            armor_upgrade_option = input(")\n")
            if armor_upgrade_option.lower() == "y":
                cls()
                War_power.training_soldier_stat()
                print_slowly(
                    f"Вы точно хотите улчучшить Броню до {armor_level_user + 1} уровня за {armor_upgrade_price}?  (Y/N")
                armor_upgrade_YN = input(")\n")
                if armor_upgrade_YN.lower() == "y":
                    cls()
                    armor_level_user += 1
                    armor_level += 1
                    print_slowly(f"Вы улучшили броню до {armor_level_user}.\n")
                    War_power.training_soldier_stat()
                    break
                elif armor_upgrade_YN.lower() == "n":
                    cls()
                    print_slowly("Вы отменили улучшение брони\n")
                    War_power.training_soldier_stat()
                    break
                else:
                    cls()
                    print_slowly("Ошибка: Введите 'Y' или 'N'.\n")
                    continue
            elif armor_upgrade_option.lower() == "n":
                cls()
                print_slowly("Отмена улучшения брони.\n")
                break
            else:
                cls()
                print_slowly("Ошибка: Введите 'Y' или 'N'.\n")
                continue


class War:
    def AI_Attack_battle():
        global soldier_AI, soldier_attack_power_AI, soldier_defense_power_AI
        global soldier, soldier_attack_power, soldier_defense_power

        soldier_attack_power_bonus = 0  # Initialize attack bonus to zero

        if soldier > soldier_AI:
            soldier_defense_power_bonus = soldier_defense_power * 0.2  # Calculate defense bonus
            soldier_defense_power += soldier_defense_power_bonus  # Apply defense bonus
        else:
            soldier_attack_power_bonus = soldier_attack_power_AI * 0.15  # Calculate attack bonus
            soldier_attack_power_AI += soldier_attack_power_bonus  # Apply attack bonus

        damage = max(soldier_attack_power_AI - soldier_defense_power, 1)  # Calculate damage with a minimum of 1
        print_slowly(f"""Солдаты врага до боя: {soldier_AI}
Солдаты до боя: {soldier}
Нажмите Enter, чтобы продолжить""")
        input(".")
        cls()
        soldier -= damage / 4
        soldier_AI -= damage
        soldier = round(soldier)
        soldier_AI = round(soldier_AI)

        if soldier_defense_power > soldier_attack_power_AI:
            soldier_attack_power_AI /= 2
            damage = max(soldier_attack_power_AI - soldier_defense_power, 1)  # Calculate damage with a minimum of 1

            soldier -= damage / 2
            soldier_AI -= damage
            soldier = round(soldier)
            soldier_AI = round(soldier_AI)
            print_slowly(f"""У вас больше защиты чем атаки у врага
Снижение атаки врага в 2 раза
Солдаты врага после боя: {soldier_AI}
Солдаты после боя: {soldier}""")
        else:
            damage = max(soldier_attack_power_AI - soldier_defense_power, 1)  # Calculate damage with a minimum of 1
            print_slowly(f"Солдаты врага до боя: {soldier_AI}\n")
            print_slowly(f"Солдаты до боя:{soldier}\n")
            soldier -= damage
            soldier_AI -= damage
            soldier = round(soldier)
            soldier_AI = round(soldier_AI)
            print_slowly(f"Солдаты врага после боя: {soldier_AI}\n")
            print_slowly(f"Солдаты после боя: {soldier}\n")

        # Reset the bonus values to the original values
        soldier_defense_power -= soldier_defense_power_bonus
        soldier_attack_power_AI -= soldier_attack_power_bonus

        if soldier <= 0 and soldier_AI >= 1:
            print_slowly("Вы проиграли.")
            exit()
        else:
            print_slowly("Вы выиграли битву\n")

    def AI_Attack():
        global soldier_attack_power_AI, soldier_defense_power
        if soldier_attack_power_AI <= soldier_defense_power / 2:
            print_slowly("Враг слишком слаб и не будет нападать в этом месяце\n")
        else:
            print_slowly("Враг нападает\n")
            battle()

#Предисловие

print_slowly(f"""____________________________
Обучение:
Управление: (Y=да;N=нет; для варианта ответа 1,2,3...; Если в конце текста есть (/) это значит что если ввести / появитса подсказка)
Возможности: управление капиталом, армией и налогами.
Препятствия: Внутренние проблемы и ВРАГ который будет нападать каждый месяц в течение года.
Цель: выдержать все атаки врага и провести контр акату.
УДАЧИ.
____________________________\n""")
Main.options_call()

#Месяц 1
print_slowly(f"{monthdict[0]}\n") #Год и название месяца
Main.stat() #Статистика

# Economic.tax()
Main.options_call()
# Economic.shop()
