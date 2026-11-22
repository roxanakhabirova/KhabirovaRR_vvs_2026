import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def make_plot_image(func, left, right, count, mode, total, x_vals, y_vals, bar_x, bar_align, step):
    # Строим график функции и прямоугольники
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=100)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8f9fa")
    ax.grid(True, linestyle="--", alpha=0.5)

    if right - left > 0:
        margin = (right - left) * 0.15
    else:
        margin = 1

    x_line = np.linspace(left - margin, right + margin, 300)
    try:
        ax.plot(x_line, func(x_line), color="#d62828", linewidth=2.5, label="f(x)")
    except Exception:
        x_line = np.linspace(left, right, 300)
        ax.plot(x_line, func(x_line), color="#d62828", linewidth=2.5, label="f(x)")

    # Ограничиваем высоту графика, чтобы асимптоты не ломали масштаб
    good_y = y_vals[np.isfinite(y_vals)]
    if len(good_y) > 0:
        limit_y = np.max(np.abs(good_y)) * 1.5
        if limit_y == 0:
            limit_y = 1.0
        ax.set_ylim(-limit_y, limit_y)

    ax.bar(
        bar_x,
        y_vals,
        width=step,
        align=bar_align,
        alpha=0.45,
        color="#4ea8de",
        edgecolor="#1d3557",
        linewidth=1,
        label="Прямоугольники (" + mode + ")",
    )

    ax.axvline(left, color="#6c757d", linestyle="--", linewidth=1.5, label="Граница L")
    ax.axvline(right, color="#6c757d", linestyle="--", linewidth=1.5, label="Граница R")

    ax.set_title("Метод: " + mode + " (N = " + str(count) + ")\nИнтеграл ≈ " + str(round(total, 5)))
    ax.legend(loc="best", fontsize=8)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close(fig)

    img = Image.open(buf)
    return img