import numpy as np

MODES = ["Левые", "Правые", "Средние"]
DEFAULT_MODE_INDEX = 2

MATH_NAMES = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "arcsin": np.arcsin,
    "arccos": np.arccos,
    "arctan": np.arctan,
    "sinh": np.sinh,
    "cosh": np.cosh,
    "tanh": np.tanh,
    "exp": np.exp,
    "log": np.log,
    "log10": np.log10,
    "sqrt": np.sqrt,
    "abs": np.absolute,
    "pi": np.pi,
    "e": np.e,
}


def check_mode(text):
    if text in MODES:
        return True
    return False


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def is_positive_int(text):
    if not text.strip().isdigit():
        return False
    if int(text.strip()) <= 0:
        return False
    return True


def check_limits(left_str, right_str):
    if not is_number(left_str) or not is_number(right_str):
        return False
    left = float(left_str)
    right = float(right_str)
    if right <= left:
        return False
    return True


def build_function(formula_text):
    formula = formula_text.strip()
    if formula == "":
        raise ValueError("Пустая формула")

    def f(x):
        x_arr = np.asarray(x, dtype=float)
        env = MATH_NAMES.copy()
        env["x"] = x_arr

        answer = eval(formula, {"__builtins__": None}, env)

        # Если пользователь ввел просто число (константу), делаем массив такого же размера
        if isinstance(answer, (int, float)):
            return np.ones_like(x_arr) * float(answer)

        return answer

    return f