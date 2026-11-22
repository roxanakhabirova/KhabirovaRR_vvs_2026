import random
from things import new_item, format_item, format_bag


def calc_attack_bonus(hero):
    # Считаем общий урон от всего оружия в рюкзаке
    bonus = 0
    for item in hero["bag"]:
        if item["kind"] == "weapon":
            if "damage" in item["stats"]:
                bonus = bonus + item["stats"]["damage"]
    return bonus


def calc_armor_block(hero):
    # Считаем общую защиту от брони
    block = 0
    for item in hero["bag"]:
        if item["kind"] == "armor":
            if "block" in item["stats"]:
                block = block + item["stats"]["block"]
    return block


def check_key(hero):
    # Проверяем, лежит ли ключ в рюкзаке
    for item in hero["bag"]:
        if item["title"] == "Ключ":
            return True
    return False


def enter_room(cell, hero, game_map, seen):
    print()
    kind = cell["kind"]

    if kind == "empty":
        print("Здесь пусто. Идем дальше.")
    elif kind == "start":
        print("Вы вернулись в начало пути.")
    elif kind == "chest":
        handle_chest(cell, hero)
    elif kind == "key":
        handle_key(cell, hero)
    elif kind == "monster":
        handle_monster(cell, hero)
    elif kind == "trap":
        handle_trap(cell, hero)
    elif kind == "portal":
        handle_portal(hero, game_map, seen)
    elif kind == "exit":
        print("Это дверь на выход! Чтобы открыть её, нужен ключ.")


def handle_chest(cell, hero):
    if len(cell["loot"]) == 0:
        print("Сундук уже пустой.")
        return

    print("Вы нашли сундук! Внутри: " + format_bag(cell["loot"]))
    choice = input("Взять всё себе? (да/нет): ").strip().lower()
    if choice != "да":
        print("Вы решили ничего не брать.")
        return

    for item in cell["loot"]:
        hero["bag"].append(item)
    print("Предметы добавлены в рюкзак (" + str(len(cell["loot"])) + " шт.).")
    cell["loot"] = []


def handle_key(cell, hero):
    if len(cell["loot"]) == 0:
        print("Ключ отсюда вы уже забрали.")
        return

    print("На полу блестит ключ!")
    choice = input("Подобрать ключ? (да/нет): ").strip().lower()
    if choice == "да":
        hero["bag"].append(cell["loot"][0])
        cell["loot"] = []
        print("Ключ теперь у вас в рюкзаке!")
    else:
        print("Вы оставили ключ лежать на полу.")


def handle_monster(cell, hero):
    if cell["extra"].get("dead") == True:
        print("Монстр в этой комнате уже побеждён.")
        return

    if "hp" not in cell["extra"]:
        cell["extra"]["hp"] = random.randint(20, 40)

    enemy_hp = cell["extra"]["hp"]
    print("На вас напал монстр! Его здоровье: " + str(enemy_hp))

    while enemy_hp > 0 and hero["hp"] > 0:
        print("Ваше HP:", hero["hp"], "| HP монстра:", enemy_hp)
        action = input("1 - ударить, 2 - выпить зелье, 3 - убежать: ").strip()

        if action == "1":
            hit = random.randint(5, 12) + calc_attack_bonus(hero)
            enemy_hp = enemy_hp - hit
            print("Вы ударили монстра на", hit, "урона!")
        elif action == "2":
            use_heal_in_fight(hero)
        elif action == "3":
            # Шанс сбежать 50 на 50
            if random.random() < 0.5:
                print("Уф, удалось убежать!")
                cell["extra"]["hp"] = enemy_hp
                return
            else:
                print("Монстр преградил путь, сбежать не вышло!")
        else:
            print("Непонятная команда, введите 1, 2 или 3.")
            continue

        # Если монстр ещё жив, он бьет в ответ
        if enemy_hp > 0:
            enemy_hit = random.randint(3, 12) - calc_armor_block(hero)
            if enemy_hit < 0:
                enemy_hit = 0
            hero["hp"] = hero["hp"] - enemy_hit
            print("Монстр ударил вас на", enemy_hit, "урона!")

    if enemy_hp <= 0:
        print("Победа над монстром!")
        cell["extra"]["dead"] = True
        reward = new_item("Золото за победу", "treasure", {"gold": 25})
        hero["bag"].append(reward)
        print("Вы получили награду: " + format_item(reward))


def use_heal_in_fight(hero):
    if len(hero["bag"]) == 0:
        print("В рюкзаке ничего нет!")
        return

    print("Ваш рюкзак:")
    for i in range(len(hero["bag"])):
        print(" ", i, "-", format_item(hero["bag"][i]))

    text = input("Введите номер предмета (или Enter для отмены): ").strip()
    if text == "":
        return

    if not text.isdigit():
        print("Нужно ввести число!")
        return

    idx = int(text)
    if idx < 0 or idx >= len(hero["bag"]):
        print("Такого номера нет!")
        return

    chosen = hero["bag"][idx]
    if chosen["kind"] == "potion":
        heal_amount = chosen["stats"].get("heal", 0)
        hero["hp"] = hero["hp"] + heal_amount
        hero["bag"].pop(idx)
        print("Вы выпили " + chosen["title"] + " и восстановили " + str(heal_amount) + " HP.")
    else:
        print("В бою можно использовать только аптечку/зелье лечения!")


def handle_trap(cell, hero):
    if cell["extra"].get("used") == True:
        print("Эта ловушка уже сломана.")
        return

    raw_dmg = random.randint(10, 25)
    shield = calc_armor_block(hero)
    real_dmg = raw_dmg - shield
    if real_dmg < 0:
        real_dmg = 0

    print("Ой, вы наступили в ловушку! Урон:", raw_dmg, "(щит поглотил:", str(shield) + ")")
    hero["hp"] = hero["hp"] - real_dmg
    cell["extra"]["used"] = True
    print("Вы потеряли", real_dmg, "HP.")


def handle_portal(hero, game_map, seen):
    rows = len(game_map)
    cols = len(game_map[0])
    other = []

    for r in range(rows):
        for c in range(cols):
            if game_map[r][c]["kind"] == "portal":
                if r != hero["row"] or c != hero["col"]:
                    other.append((r, c))

    if len(other) == 0:
        print("Портал не работает — других порталов на карте нет.")
        return

    target = random.choice(other)
    print("Вас затянуло в портал! Перенос в клетку (" + str(target[0]) + ", " + str(target[1]) + ")")
    hero["row"] = target[0]
    hero["col"] = target[1]
    seen[target[0]][target[1]] = True


def buff_weapon_with_mana(hero, mana_idx, weapon_idx):
    mana_item = hero["bag"][mana_idx]
    weapon_item = hero["bag"][weapon_idx]

    if mana_item["kind"] != "mana_potion":
        print("Это не эликсир маны!")
        return
    if weapon_item["kind"] != "weapon":
        print("Усилить можно только оружие!")
        return

    plus_dmg = mana_item["stats"].get("mana", 10)
    old_dmg = weapon_item["stats"].get("damage", 0)
    weapon_item["stats"]["damage"] = old_dmg + plus_dmg
    hero["bag"].pop(mana_idx)
    print("Оружие усилено! Урон был", old_dmg, "-> стал", old_dmg + plus_dmg)


def drink_heal_outside(hero, idx):
    if idx < 0 or idx >= len(hero["bag"]):
        print("Неверный номер!")
        return

    item = hero["bag"][idx]
    if item["kind"] != "potion":
        print("Это не лечебное зелье!")
        return

    heal = item["stats"].get("heal", 0)
    hero["hp"] = hero["hp"] + heal
    hero["bag"].pop(idx)
    print("Вы поправили здоровье на", heal, "HP. Теперь у вас", hero["hp"], "HP.")
