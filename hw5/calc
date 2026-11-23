DISCOUNTS = {
    "Без скидки (0%)": 0,
    "Обычная карта (5%)": 5,
    "Серебряная карта (10%)": 10,
    "Золотая карта (20%)": 20,
}


def check_numbers(price_text, count_text):
    price_text = price_text.strip().replace(",", ".")
    count_text = count_text.strip()

    if price_text == "" or count_text == "":
        return False, "Заполните оба поля!"

    # Проверяем, что цена — положительное число (допускаем одну точку)
    if not price_text.replace(".", "", 1).isdigit():
        return False, "Цена должна быть положительным числом!"

    if not count_text.isdigit() or int(count_text) <= 0:
        return False, "Количество должно быть целым числом больше 0!"

    price = float(price_text)
    if price <= 0:
        return False, "Цена должна быть больше нуля!"

    return True, (price, int(count_text))


def calc_discount(price, count, card_name, has_promo):
    percent = DISCOUNTS[card_name]
    if has_promo:
        percent = percent + 5

    full_sum = price * count
    saved = full_sum * percent / 100
    final_sum = full_sum - saved

    return round(final_sum, 2), round(saved, 2)