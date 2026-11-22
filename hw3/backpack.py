import copy
from things import format_item, format_bag
from room_events import buff_weapon_with_mana, drink_heal_outside

KIND_PRIORITY = {
    "weapon": 0,
    "armor": 1,
    "potion": 2,
    "mana_potion": 3,
    "key": 4,
    "scroll": 5,
    "treasure": 6,
}


def item_sort_key(item):
    # Сначала сортируем по типу, потом по названию
    priority = KIND_PRIORITY.get(item["kind"], 99)
    return (priority, item["title"])


def search_item_index(hero, target_name):
    # Ищем индекс предмета по названию
    for i in range(len(hero["bag"])):
        if hero["bag"][i]["title"] == target_name:
            return i
    return -1


def bag_menu(hero):
    while True:
        print()
        print("--- ВАШ РЮКЗАК ---")
        if len(hero["bag"]) == 0:
            print("Рюкзак пуст.")
            print("0 - вернуться в игру")
            cmd = input("> ").strip()
            if cmd == "0":
                return
            continue

        for i in range(len(hero["bag"])):
            print(" ", i, ":", format_item(hero["bag"][i]))

        print("Что сделать?")
        print(" 1 - выбросить предмет по названию")
        print(" 2 - выбросить предмет по номеру")
        print(" 3 - отсортировать (тип и название)")
        print(" 4 - отсортировать в обратном порядке")
        print(" 5 - перевернуть список предметов")
        print(" 6 - найти предмет по названию")
        print(" 7 - сделать копию и показать первые 3 (срез)")
        print(" 8 - тест: copy() против deepcopy()")
        print(" 9 - использовать предмет")
        print(" 0 - вернуться в игру")

        cmd = input("> ").strip()

        if cmd == "0":
            return

        elif cmd == "1":
            name = input("Введите точное название предмета: ").strip()
            found = False
            for item in hero["bag"]:
                if item["title"] == name:
                    hero["bag"].remove(item)
                    print("Выброшено: " + format_item(item))
                    found = True
                    break
            if not found:
                print("Такого предмета в рюкзаке нет.")

        elif cmd == "2":
            text = input("Введите номер предмета: ").strip()
            if not text.isdigit():
                print("Нужно ввести целое число!")
                continue
            idx = int(text)
            if idx < 0 or idx >= len(hero["bag"]):
                print("Нет предмета с таким номером!")
                continue
            dropped = hero["bag"].pop(idx)
            print("Выброшено: " + format_item(dropped))

        elif cmd == "3":
            hero["bag"].sort(key=item_sort_key)
            print("Рюкзак отсортирован!")

        elif cmd == "4":
            hero["bag"].sort(key=item_sort_key, reverse=True)
            print("Рюкзак отсортирован по убыванию!")

        elif cmd == "5":
            hero["bag"].reverse()
            print("Порядок предметов перевёрнут!")

        elif cmd == "6":
            name = input("Что ищем? ").strip()
            pos = search_item_index(hero, name)
            if pos == -1:
                print("Ничего не найдено.")
            else:
                print("Предмет найден под номером", pos, ":", format_item(hero["bag"][pos]))

        elif cmd == "7":
            bag_copy = hero["bag"].copy()
            print()
            print("Всего в копии предметов:", len(bag_copy))
            print("Копия:", format_bag(bag_copy))

            top_three = bag_copy[:3]
            print("Первые три предмета:", format_bag(top_three))
            print("Помните: .copy() делает только поверхностную копию списка!")

        elif cmd == "8":
            show_copy_vs_deepcopy(hero)

        elif cmd == "9":
            print("Какой предмет использовать?")
            for i in range(len(hero["bag"])):
                print(" ", i, ":", format_item(hero["bag"][i]))

            ans1 = input("Номер предмета: ").strip()
            if not ans1.isdigit():
                print("Нужно ввести число!")
                continue
            idx1 = int(ans1)
            if idx1 < 0 or idx1 >= len(hero["bag"]):
                print("Неверный номер!")
                continue

            item1 = hero["bag"][idx1]
            if item1["kind"] == "potion":
                drink_heal_outside(hero, idx1)
            elif item1["kind"] == "mana_potion":
                ans2 = input("К какому оружию применить? Введите номер: ").strip()
                if not ans2.isdigit():
                    print("Нужно ввести число!")
                    continue
                idx2 = int(ans2)
                if idx2 < 0 or idx2 >= len(hero["bag"]):
                    print("Неверный номер!")
                    continue
                buff_weapon_with_mana(hero, idx1, idx2)
            else:
                print("Этот предмет нельзя использовать.")

        else:
            print("Неизвестная команда.")


def show_copy_vs_deepcopy(hero):
    if len(hero["bag"]) == 0:
        print("Рюкзак пустой, нечего тестировать.")
        return

    # Ищем первый предмет, у которого есть характеристики в stats
    target_idx = -1
    for i in range(len(hero["bag"])):
        if len(hero["bag"][i]["stats"]) > 0:
            target_idx = i
            break

    if target_idx == -1:
        print("Нет предметов с характеристиками для теста.")
        return

    stat_name = ""
    for k in hero["bag"][target_idx]["stats"]:
        stat_name = k
        break

    old_val = hero["bag"][target_idx]["stats"][stat_name]

    print()
    print("=== СРАВНЕНИЕ copy() И deepcopy() ===")
    print("Берем предмет:", format_item(hero["bag"][target_idx]))

    # 1. Поверхностная копия
    shallow_copy = hero["bag"].copy()
    shallow_copy[target_idx]["stats"][stat_name] = old_val + 100
    print("После изменения copy():")
    print(" Копия:   ", format_bag(shallow_copy))
    print(" Оригинал:", format_bag(hero["bag"]))

    if hero["bag"][target_idx]["stats"][stat_name] == old_val + 100:
        print("-> Оригинал тоже поменялся! Потому что словари внутри общие.")
        # Возвращаем старое значение обратно
        hero["bag"][target_idx]["stats"][stat_name] = old_val

    # 2. Глубокая копия
    deep_copy = copy.deepcopy(hero["bag"])
    deep_copy[target_idx]["stats"][stat_name] = old_val + 100
    print()
    print("После изменения deepcopy():")
    print(" Копия:   ", format_bag(deep_copy))
    print(" Оригинал:", format_bag(hero["bag"]))

    if hero["bag"][target_idx]["stats"][stat_name] == old_val:
        print("-> Оригинал остался прежним! deepcopy() скопировал всё полностью.")
