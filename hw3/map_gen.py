import random
import copy
from things import new_item

# Обозначения клеток на карте
SYMBOLS = {
    "start": "S",
    "exit": "E",
    "empty": ".",
    "chest": "C",
    "monster": "M",
    "trap": "T",
    "key": "K",
    "portal": "P",
}

HERO_SIGN = "@"
FOG_SIGN = "#"

POSSIBLE_ROOMS = ["empty", "chest", "monster", "trap", "portal"]

# Возможные находки в сундуках
LOOT_LIST = [
    ("Мешок золота", "treasure", {"gold": 50}),
    ("Аптечка", "potion", {"heal": 30}),
    ("Эликсир маны", "mana_potion", {"mana": 10}),
    ("Железный меч", "weapon", {"damage": 10}),
    ("Деревянный щит", "armor", {"block": 5}),
    ("Старый свиток", "scroll", {}),
]


def build_map(rows, cols):
    # Создаем сетку комнат
    game_map = []
    seen = []

    for r in range(rows):
        map_row = []
        seen_row = []
        for c in range(cols):
            room_kind = random.choice(POSSIBLE_ROOMS)
            cell = {
                "kind": room_kind,
                "loot": [],
                "extra": {},
            }
            map_row.append(cell)
            seen_row.append(False)
        game_map.append(map_row)
        seen.append(seen_row)

    # Старт в левом верхнем углу, выход в правом нижнем
    game_map[0][0]["kind"] = "start"
    game_map[rows - 1][cols - 1]["kind"] = "exit"

    # Ищем свободные клетки, чтобы спрятать ключ
    free_cells = []
    for r in range(rows):
        for c in range(cols):
            if (r == 0 and c == 0) or (r == rows - 1 and c == cols - 1):
                continue
            free_cells.append((r, c))

    key_r, key_c = random.choice(free_cells)
    game_map[key_r][key_c]["kind"] = "key"
    game_map[key_r][key_c]["loot"] = [new_item("Ключ", "key", {})]

    # Заполняем сундуки предметами
    for r in range(rows):
        for c in range(cols):
            if game_map[r][c]["kind"] == "chest":
                # Иногда сундук оказывается пустым
                if random.random() < 0.3:
                    game_map[r][c]["loot"] = []
                else:
                    how_many = random.randint(1, 3)
                    picked = random.sample(LOOT_LIST, how_many)
                    chest_items = []
                    for title, kind, stats in picked:
                        # Используем deepcopy, чтобы у каждого предмета был свой словарь stats
                        chest_items.append(new_item(title, kind, copy.deepcopy(stats)))
                    game_map[r][c]["loot"] = chest_items

    return game_map, seen


def draw_map(game_map, seen, hero_pos, rows, cols):
    for r in range(rows):
        line = ""
        for c in range(cols):
            if (r, c) == hero_pos:
                line = line + HERO_SIGN + " "
            elif seen[r][c]:
                kind = game_map[r][c]["kind"]
                line = line + SYMBOLS[kind] + " "
            else:
                line = line + FOG_SIGN + " "
        print(line)
