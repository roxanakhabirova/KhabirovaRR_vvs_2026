def task1():
    ex = "пРоГрАмМиРоВаНиЕ"
    print("")
    print("Уровень 1! Здесь разберем 3 метода для смены регистра букв:")
    print("1) upper() - делает все буквы большими")
    print("2) lower() - делает все буквы маленькими")
    print("3) capitalize() - делает большой только первую букву, а остальные маленькими")
    print("")
    print("Посмотрим на примере строки:", ex)
    print("upper():", ex.upper())
    print("lower():", ex.lower())
    print("capitalize():", ex.capitalize())
    print("")

    try:
        mode = int(input("Введите номер метода (1, 2 или 3): "))
        if mode == 1:
            text = input("Введите вашу строку: ")
            print("Ответ:", text.upper())
        elif mode == 2:
            text = input("Введите вашу строку: ")
            print("Ответ:", text.lower())
        elif mode == 3:
            text = input("Введите вашу строку: ")
            print("Ответ:", text.capitalize())
        else:
            print("Такого номера нет!")
    except ValueError:
        print("Ошибка! Нужно ввести число.")


def task2():
    ex = "Писать код интересно. Очень интересно"
    print("")
    print("Уровень 2! Здесь разберем 3 метода для работы с подстроками:")
    print("1) find(слово) - ищет, где впервые встречается слово (или выдает -1)")
    print("2) replace(старое, новое, сколько_раз) - заменяет кусок текста на другой")
    print("3) count(слово) - считает, сколько раз слово встретилось в тексте")
    print("")
    print("Посмотрим на примере строки:", ex)
    print('Ищем слово "интересно" (find):', ex.find("интересно"))
    print('Меняем "интересно" на "полезно" (replace):', ex.replace("интересно", "полезно"))
    print('Считаем букву "е" (count):', ex.count("е"))
    print("")

    try:
        mode = int(input("Введите номер метода (1, 2 или 3): "))
        if mode == 1:
            text = input("Введите строку: ")
            word = input("Что нужно найти? ")
            print("Ответ:", text.find(word))
        elif mode == 2:
            text = input("Введите строку: ")
            old_word = input("Что нужно заменить? ")
            new_word = input("На что заменить? ")
            cnt = int(input("Сколько раз заменить (напишите -1, если нужно все): "))
            if cnt == -1:
                print("Ответ:", text.replace(old_word, new_word))
            elif cnt >= 0:
                print("Ответ:", text.replace(old_word, new_word, cnt))
            else:
                print("Число замен не может быть меньше -1!")
        elif mode == 3:
            text = input("Введите строку: ")
            word = input("Что нужно посчитать? ")
            print("Ответ:", text.count(word))
        else:
            print("Такого номера нет!")
    except ValueError:
        print("Ошибка! Нужно ввести число.")


def task3():
    ex1 = "яблоко;груша;слива"
    ex2 = ["яблоко", "груша", "слива"]
    print("")
    print("Уровень 3! Здесь разберем split и join:")
    print("1) split(знак) - делит строку на список по указанному знаку")
    print("2) знак.join(список) - соединяет элементы списка обратно в одну строку")
    print("")
    print("Пример со строкой:", ex1)
    print('Делим по ";" (split):', ex1.split(";"))
    print("")
    print("Пример со списком:", ex2)
    print('Собираем через ";" (join):', ";".join(ex2))
    print("")

    try:
        mode = int(input("Введите номер метода (1 или 2): "))
        if mode == 1:
            text = input("Введите строку: ")
            sep = input("Введите разделитель: ")
            if sep == "":
                print("Ответ:", text.split())
            else:
                print("Ответ:", text.split(sep))
        elif mode == 2:
            n = int(input("Сколько элементов будет в списке? "))
            if n < 1:
                print("Должен быть хотя бы 1 элемент!")
            else:
                arr = []
                for i in range(n):
                    elem = input("Введите элемент: ")
                    arr.append(elem)
                sep = input("Введите разделитель (можно оставить пустым): ")
                print("Ответ:", sep.join(arr))
        else:
            print("Такого номера нет!")
    except ValueError:
        print("Ошибка! Нужно ввести число.")


def task4():
    ex1 = "2026_test!"
    ex2 = "   привет мир   "
    print("")
    print("Уровень 4! Проверка строки и очистка лишнего:")
    print("1) isdigit() - проверяет, только ли цифры в строке")
    print("2) isalpha() - проверяет, только ли буквы в строке")
    print("3) strip(символы) - убирает пробелы или указанные символы по краям")
    print("")
    print("Пример проверки строки:", ex1)
    print("isdigit():", ex1.isdigit())
    print("isalpha():", ex1.isalpha())
    print("")
    print("Пример очистки строки:", ex2)
    print("strip():", ex2.strip())
    print("")

    try:
        mode = int(input("Введите номер метода (1, 2 или 3): "))
        if mode == 1:
            text = input("Введите строку: ")
            print("Ответ:", text.isdigit())
        elif mode == 2:
            text = input("Введите строку: ")
            print("Ответ:", text.isalpha())
        elif mode == 3:
            text = input("Введите строку: ")
            chars = input("Какие символы убрать по краям (Enter для пробелов)? ")
            if chars == "":
                print("Ответ:", text.strip())
            else:
                print("Ответ:", text.strip(chars))
        else:
            print("Такого номера нет!")
    except ValueError:
        print("Ошибка! Нужно ввести число.")


def clean_text(text):
    words = text.split()
    s = " ".join(words)

    for p in [".", ",", ":", ";", "!", "?"]:
        s = s.replace(" " + p, p)
        s = s.replace(p, p + " ")

    s = " ".join(s.split())

    res = ""
    big = True
    for ch in s:
        if big == True and ch.isalpha():
            res = res + ch.upper()
            big = False
        else:
            res = res + ch.lower()
            if ch == "." or ch == "!" or ch == "?":
                big = True
            elif ch != " ":
                big = False
    return res


def task5():
    ex = "   пРиВеТ;мир!как   дела?нормально.  "
    print("")
    print("Уровень 5! Умный редактор текста.")
    print("Он убирает лишние пробелы, поправляет знаки препинания и заглавные буквы.")
    print("")
    print("Было:", ex)
    print("Стало:", clean_text(ex))
    print("")
    user_text = input("Введите текст, который нужно исправить: ")
    print("Ответ:", clean_text(user_text))
