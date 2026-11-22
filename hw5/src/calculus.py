import numpy as np


def calc_integral(func, left, right, count, mode):
    # Считаем ширину одного прямоугольника
    step = (right - left) / count
    points = np.linspace(left, right, count + 1)

    if mode == "Левые":
        x_vals = points[:-1]
        bar_align = "edge"
        bar_x = x_vals
    elif mode == "Правые":
        x_vals = points[1:]
        bar_align = "edge"
        bar_x = x_vals - step
    else:
        # Для средних прямоугольников берем середину каждого отрезка
        x_vals = points[:-1] + step / 2
        bar_align = "center"
        bar_x = x_vals

    y_vals = func(x_vals)

    # Отбрасываем бесконечности и NaN, если они попались при делении на 0
    good = np.isfinite(y_vals)
    total = np.sum(y_vals[good]) * step

    return total, x_vals, y_vals, bar_x, bar_align, step
