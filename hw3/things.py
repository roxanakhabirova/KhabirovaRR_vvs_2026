def new_item(title, kind, stats):
    # Создаем словарь для предмета
    return {
        "title": title,
        "kind": kind,
        "stats": stats,
    }


def format_item(item):
    # Превращаем один предмет в красивую строку
    text = item["title"] + " (" + item["kind"] + ")"
    if len(item["stats"]) > 0:
        parts = []
        for key in item["stats"]:
            val = item["stats"][key]
            parts.append(key + ": " + str(val))
        text = text + " [" + ", ".join(parts) + "]"
    return text


def format_bag(bag):
    # Выводим весь список предметов одной строкой
    if len(bag) == 0:
        return "пусто"
    result = []
    for elem in bag:
        result.append(format_item(elem))
    return ", ".join(result)
