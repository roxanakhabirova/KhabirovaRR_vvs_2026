import func

go = "да"
while go != "нет":
    print("")
    print("Выберите уровень от 1 до 5:")
    print("1 - Изменение регистра")
    print("2 - Поиск и замена")
    print("3 - Split и Join")
    print("4 - Проверка и очистка")
    print("5 - Умный редактор")

    try:
        lvl = int(input("Номер уровня: "))
        if lvl == 1:
            func.task1()
        elif lvl == 2:
            func.task2()
        elif lvl == 3:
            func.task3()
        elif lvl == 4:
            func.task4()
        elif lvl == 5:
            func.task5()
        else:
            print("Такого уровня нет!")
    except ValueError:
        print("Ошибка! Нужно ввести цифру.")

    go = input('Хотите продолжить? Напишите "да" или "нет": ').strip().lower()
