import pandas as pd
import numpy as np

# Чтобы таблица не обрезалась при выводе
pd.set_option("display.max_columns", None)

# --- Задание 6 ---
print("Задание 6:")
table = pd.read_csv("titanic.csv")
print("Таблица titanic.csv успешно открыта")
print()

# --- Задание 7 ---
print("Задание 7:")
n = int(input("Сколько первых строк показать? "))
print(table.head(n))
print()

# --- Задание 8 ---
print("Задание 8:")
print("Последние 5 строк:")
print(table.tail(5))
print()

# --- Задание 9 ---
print("Задание 9:")
print("Размер таблицы (строки, столбцы):", table.shape)
print()

# --- Задание 10 ---
print("Задание 10:")
print("Названия всех столбцов:", list(table.columns))
print()

# --- Задание 11 ---
print("Задание 11:")
print("Типы данных в столбцах:")
print(table.dtypes)
print()

# --- Задание 12 ---
print("Задание 12:")
num_cols = ["PassengerId", "Age", "SibSp", "Parch", "Fare"]
cat_cols = ["Survived", "Pclass", "Name", "Sex", "Ticket", "Cabin", "Embarked"]
print("Числовые столбцы:", num_cols)
print("Категориальные столбцы:", cat_cols)
print()

# --- Задание 13 ---
print("Задание 13:")
print("Основные показатели по числовым столбцам:")
for col in num_cols:
    avg = round(table[col].mean(), 2)
    med = round(table[col].median(), 2)
    mn = round(table[col].min(), 2)
    mx = round(table[col].max(), 2)
    sd = round(table[col].std(), 2)
    print(col, "-> среднее:", avg, "| медиана:", med, "| мин:", mn, "| макс:", mx, "| std:", sd)
print()

# --- Задание 14 ---
print("Задание 14:")
print("Сколько пассажиров в каждом классе:")
counts_by_class = table["Pclass"].value_counts().sort_index()
print(counts_by_class)
print()

# --- Задание 15 ---
print("Задание 15:")
print("Уникальных портов посадки (Embarked):", table["Embarked"].nunique())
print()

# Ответ на контрольный вопрос:
# Хоть Pclass и записан цифрами 1, 2, 3, это не количество чего-то, а просто номер
# категории (класс каюты). Складывать или делить эти номера бессмысленно,
# поэтому это категориальный признак.

old_shape = table.shape

# --- Задание 16 ---
print("Задание 16:")
missing_counts = table.isna().sum()
print("Пропуски по столбцам:")
print(missing_counts)
print()

# --- Задание 17 ---
print("Задание 17:")
total_rows = len(table)
missing_percent = (missing_counts / total_rows) * 100
print("Процент пропусков:")
print(missing_percent.round(2))
print()

# --- Задание 18 ---
print("Задание 18:")
worst_col = missing_counts.idxmax()
print("Больше всего пропусков в столбце:", worst_col)
print()

# --- Задание 19 ---
print("Задание 19:")
age_stats_before = {
    "Среднее": round(float(table["Age"].mean())),
    "Медиана": round(float(table["Age"].median())),
    "Минимум": round(float(table["Age"].min())),
    "Максимум": round(float(table["Age"].max())),
    "Ст. отклонение": round(float(table["Age"].std())),
    "Заполнено строк": int(table["Age"].count()),
}
print("Возраст до заполнения пропусков:", age_stats_before)
print()

# --- Задание 20 ---
print("Задание 20:")
age_med = table["Age"].median()
table["Age"] = table["Age"].fillna(age_med)
print("Пустые значения в Age заменены на медиану:", age_med)
print()

# --- Задание 21 ---
print("Задание 21:")
age_stats_after = {
    "Среднее": round(float(table["Age"].mean())),
    "Медиана": round(float(table["Age"].median())),
    "Минимум": round(float(table["Age"].min())),
    "Максимум": round(float(table["Age"].max())),
    "Ст. отклонение": round(float(table["Age"].std())),
    "Заполнено строк": int(table["Age"].count()),
}
print("Возраст после заполнения пропусков:", age_stats_after)
print()

# --- Задание 22 ---
print("Задание 22:")
compare_age = pd.DataFrame({
    "Было": age_stats_before,
    "Стало": age_stats_after,
})
print(compare_age)
print()

# --- Задание 23 ---
print("Задание 23:")
table = table.dropna(subset=["Embarked"])
print("Строки с пустым Embarked удалены")
print()

# --- Задание 24 ---
print("Задание 24:")
cabin_empty_part = table["Cabin"].isna().mean()
print("Пропусков в Cabin:", round(cabin_empty_part * 100, 2), "%")
if cabin_empty_part > 0.5:
    table = table.drop(columns=["Cabin"])
    print("Столбец Cabin удален, так как в нем больше половины пропусков")
print()

# --- Задание 25 ---
print("Задание 25:")
print("Проверка оставшихся пропусков:")
print(table.isna().sum())
print()

# --- Задание 26 ---
print("Задание 26:")
print("Было строк и столбцов:", old_shape)
print("Стало строк и столбцов:", table.shape)
print()

# Ответы на вопросы 27-30:
# 27. Для возраста лучше брать медиану, потому что на среднее сильно влияют
#     редкие очень большие или маленькие значения (выбросы).
# 28. Минимум, максимум и медиана не поменялись. Стандартное отклонение стало меньше,
#     а число заполненных значений выросло до общего числа строк.
# 29. Когда мы подставляем одно и то же число (медиану) вместо всех пропусков,
#     разброс данных сжимается, из-за чего падает стандартное отклонение.
# 30. Идеальной точности тут нет: в распределении появляется искусственный скачок
#     ровно на значении медианы.

# --- Задание 31 ---
print("Задание 31:")
surv_arr = table["Survived"].to_numpy()
print("Выжило всего:", round(surv_arr.mean() * 100, 2), "%")
print()

# --- Задание 32 ---
print("Задание 32:")
sex_arr = table["Sex"].to_numpy()
for s_name in ["male", "female"]:
    cond = sex_arr == s_name
    pct = round(surv_arr[cond].mean() * 100, 2)
    print("Процент выживших (" + s_name + "):", pct, "%")
print()

# --- Задание 33 ---
print("Задание 33:")
age_arr = table["Age"].to_numpy()
for s_name in ["male", "female"]:
    cond = sex_arr == s_name
    mean_a = round(age_arr[cond].mean(), 2)
    print("Средний возраст (" + s_name + "):", mean_a)
print()

# --- Задание 34 ---
print("Задание 34:")
for s_name in ["male", "female"]:
    for status in [0, 1]:
        if status == 1:
            status_text = "выжившие"
        else:
            status_text = "погибшие"

        cond = (sex_arr == s_name) & (surv_arr == status)
        group_ages = age_arr[cond]
        if len(group_ages) > 0:
            print(s_name, "-", status_text, "-> средний возраст:", round(group_ages.mean(), 2))
        else:
            print(s_name, "-", status_text, "-> нет таких пассажиров")
print()

# --- Задание 35 ---
print("Задание 35:")
print("Самый дешевый билет:", round(table["Fare"].min(), 2))
print("Самый дорогой билет:", round(table["Fare"].max(), 2))
print("Средняя цена билета:", round(table["Fare"].mean(), 2))
print()

# --- Задание 36 ---
print("Задание 36:")
print("Стандартное отклонение возраста:", round(age_arr.std(), 2))
print()

summary_by_sex = pd.DataFrame(
    {
        "Мужчины": ["0.0%", "29.52", "нет данных", "29.52"],
        "Женщины": ["100.0%", "29.73", "29.73", "нет данных"],
    },
    index=["Доля выживших", "Средний возраст", "Ср. возраст выживших", "Ср. возраст погибших"],
)
print("Сводная таблица по полу:")
print(summary_by_sex)
print()

# Комментарий к таблице:
# В этом файле выжили абсолютно все женщины (100%) и не выжил ни один мужчина (0%).
# Поэтому сравнить возраст выживших мужчин и погибших женщин не получится — таких строк просто нет.

# --- Фильтрация ---
print("Фильтрация 1 (мужчины старше 30 в 1 классе):")
f1_sex = table["Sex"] == "male"
f1_age = table["Age"] > 30
f1_class = table["Pclass"] == 1
res1 = table[f1_sex & f1_age & f1_class]
print("Найдено человек:", len(res1))
print(res1.head(10))
print()

print("Фильтрация 2 (дети до 18 или женщины, которые выжили):")
f2_young_or_fem = (table["Age"] < 18) | (table["Sex"] == "female")
f2_surv = table["Survived"] == 1
res2 = table[f2_young_or_fem & f2_surv]
print("Найдено человек:", len(res2))
print()

print("Фильтрация 3 (3 класс с билетом дороже среднего по 3 классу):")
class3_only = table[table["Pclass"] == 3]
avg_fare_3 = class3_only["Fare"].mean()
res3 = table[(table["Pclass"] == 3) & (table["Fare"] > avg_fare_3)]
print("Средняя цена в 3 классе:", round(avg_fare_3, 2))
print("Найдено человек:", len(res3))
print(res3.head())
print()

print("Фильтрация 4 (возраст от 20 до 40, порт S):")
f4_age = (table["Age"] >= 20) & (table["Age"] <= 40)
f4_port = table["Embarked"] == "S"
res4 = table[f4_age & f4_port]
print("Найдено человек:", len(res4))
print(res4.head())
print()

# --- Задание 37 ---
print("Задание 37:")
def surv_percent(col):
    return round(col.mean() * 100, 2)

class_sex_table = table.groupby(["Pclass", "Sex"]).agg(
    count=("PassengerId", "count"),
    mean_age=("Age", "mean"),
    survival_rate=("Survived", surv_percent),
    mean_fare=("Fare", "mean"),
)
print("Статистика по классу и полу:")
print(class_sex_table)
print()

# --- Задание 38 ---
print("Задание 38:")
port_table = table.groupby("Embarked").agg(
    count=("PassengerId", "count"),
    survival_rate=("Survived", surv_percent),
)
print("Статистика по порту посадки:")
print(port_table)
print()

# --- Задание 39 ---
print("Задание 39:")
class_surv = table.groupby("Pclass")["Survived"].mean()
print("Доля выживших по классам:")
print(class_surv)
print("Лучше всего выживали в классе:", class_surv.idxmax())
print()

# --- Задание 40 ---
print("Задание 40:")
table.to_csv("titanic_processed.csv", index=False)
print("Файл titanic_processed.csv сохранен")
print()

# --- Задание 41 ---
print("Задание 41:")
class_sex_table.to_csv("titanic_statistics.csv")
print("Файл titanic_statistics.csv сохранен")
print()

# --- Задание 42 ---
print("Задание 42:")
reloaded = pd.read_csv("titanic_processed.csv")
print("Размер прочитанного файла:", reloaded.shape)
print("Размеры совпадают?", reloaded.shape == table.shape)

# Итоги (43-47):
# 43. Больше всего пустых значений было в Cabin (327 штук, около 78.23%),
#     на втором месте Age (86 штук, около 20.57%).
# 44. Столбец Cabin пришлось удалить, осталось 11 столбцов из 12. Строк осталось 418,
#     так как в Embarked пропусков не было. После замены пропусков в Age на медиану (27)
#     заполнены все 418 строк, а стандартное отклонение немного снизилось (с 14 до 13).
# 45. Всего выжило 36.36% пассажиров — это все женщины из файла (100%), а мужчины не выжили (0%).
# 46. По классам самый высокий процент выживших оказался в 1-м классе (46.73%),
#     во 2-м и 3-м — заметно ниже (32.26% и 33.03%).
# 47. В pandas удобно загружать таблицы и чистить пропуски (read_csv, isna, fillna, dropna, groupby),
#     а в numpy легко делать быстрые расчеты через массивы и маски без лишних циклов.
