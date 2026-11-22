def create_hero(start_row, start_col):
    # Начальные параметры игрока
    hero = {
        "row": start_row,
        "col": start_col,
        "hp": 100,
        "bag": [],
    }
    return hero


def get_coords(hero):
    return (hero["row"], hero["col"])


def move_hero(hero, direction, rows, cols):
    # Пробуем сдвинуть игрока по кнопкам w/a/s/d
    new_r = hero["row"]
    new_c = hero["col"]

    if direction == "w":
        new_r = new_r - 1
    elif direction == "s":
        new_r = new_r + 1
    elif direction == "a":
        new_c = new_c - 1
    elif direction == "d":
        new_c = new_c + 1
    else:
        return False

    # Проверяем, не вышли ли за границы поля
    if new_r < 0 or new_r >= rows:
        return False
    if new_c < 0 or new_c >= cols:
        return False

    hero["row"] = new_r
    hero["col"] = new_c
    return True
