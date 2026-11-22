from map_gen import build_map, draw_map
from hero import create_hero, get_coords, move_hero
from things import format_bag
from room_events import enter_room, check_key
from backpack import bag_menu


def start_game():
    rows = 10
    cols = 10
    game_map, seen = build_map(rows, cols)
    hero = create_hero(0, 0)
    seen[0][0] = True

    while True:
        print()
        draw_map(game_map, seen, get_coords(hero), rows, cols)

        if check_key(hero):
            key_status = "есть"
        else:
            key_status = "нет"

        print("Здоровье:", hero["hp"], "| Ключ:", key_status)
        print("Рюкзак:", format_bag(hero["bag"]))
        print("Управление: w/a/s/d - шаг, i - рюкзак, q - выход")

        command = input("Введите команду: ").strip().lower()

        if command == "q":
            print("Вы вышли из игры.")
            break

        if command == "i":
            bag_menu(hero)
            continue

        moved = move_hero(hero, command, rows, cols)
        if not moved:
            print("Туда пройти нельзя!")
            continue

        cur_r, cur_c = get_coords(hero)

        # Проверяем условие победы
        if cur_r == rows - 1 and cur_c == cols - 1 and check_key(hero):
            print()
            print("****************************************")
            print("  ПОБЕДА! Вы нашли ключ и открыли выход!")
            print("****************************************")
            break

        if not seen[cur_r][cur_c]:
            seen[cur_r][cur_c] = True
            enter_room(game_map[cur_r][cur_c], hero, game_map, seen)
            if hero["hp"] <= 0:
                print()
                print("Игра окончена, вы погибли. HP:", hero["hp"])
                break


start_game()
