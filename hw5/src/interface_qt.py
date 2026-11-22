import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PIL.ImageQt import ImageQt

import validators
from calculus import calc_integral
from vis import make_plot_image
from styles import APP_STYLE, ERROR_STYLE


class ErrorPopup(QtWidgets.QDialog):
    def __init__(self, parent=None, message="Произошла ошибка"):
        super().__init__(parent)
        self.setWindowTitle("Ошибка ввода")
        self.resize(320, 140)
        self.setStyleSheet(ERROR_STYLE)

        box = QtWidgets.QVBoxLayout()
        self.text_label = QtWidgets.QLabel(message)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setWordWrap(True)

        self.ok_btn = QtWidgets.QPushButton("Понятно")
        self.ok_btn.clicked.connect(self.accept)

        box.addWidget(self.text_label)
        box.addWidget(self.ok_btn)
        self.setLayout(box)


class IntegralApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Калькулятор интегралов")
        self.resize(950, 620)
        self.setStyleSheet(APP_STYLE)

        main_box = QtWidgets.QVBoxLayout()

        # Верхняя панель с результатом
        top_group = QtWidgets.QGroupBox("Результат")
        top_row = QtWidgets.QHBoxLayout()

        self.title_lbl = QtWidgets.QLabel("Численное интегрирование")
        self.result_lbl = QtWidgets.QLabel("Ответ: пока не посчитано")

        top_row.addWidget(self.title_lbl)
        top_row.addWidget(self.result_lbl)
        top_group.setLayout(top_row)
        main_box.addWidget(top_group)

        # Область для графика
        plot_group = QtWidgets.QGroupBox("График")
        plot_row = QtWidgets.QHBoxLayout()

        self.pic_label = QtWidgets.QLabel()
        self.pic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        plot_row.addWidget(self.pic_label)
        plot_group.setLayout(plot_row)
        main_box.addWidget(plot_group)

        # Нижняя панель ввода
        controls_group = QtWidgets.QGroupBox("Параметры")
        controls_row = QtWidgets.QHBoxLayout()

        self.mode_box = QtWidgets.QComboBox()
        self.mode_box.addItems(validators.MODES)
        self.mode_box.setCurrentIndex(validators.DEFAULT_MODE_INDEX)

        self.left_edit = QtWidgets.QLineEdit()
        self.left_edit.setPlaceholderText("Левая граница L")

        self.right_edit = QtWidgets.QLineEdit()
        self.right_edit.setPlaceholderText("Правая граница R")

        self.n_edit = QtWidgets.QLineEdit()
        self.n_edit.setPlaceholderText("Число N")

        self.formula_edit = QtWidgets.QPlainTextEdit()
        self.formula_edit.setPlaceholderText("Например: x**2 + sin(x)")
        self.formula_edit.setMaximumHeight(55)

        self.calc_btn = QtWidgets.QPushButton("Посчитать")
        self.calc_btn.clicked.connect(self.calculate_click)

        controls_row.addWidget(self.mode_box)
        controls_row.addWidget(self.left_edit)
        controls_row.addWidget(self.right_edit)
        controls_row.addWidget(self.n_edit)
        controls_row.addWidget(self.formula_edit)
        controls_row.addWidget(self.calc_btn)

        controls_group.setLayout(controls_row)
        main_box.addWidget(controls_group)

        self.setLayout(main_box)

    def show_error(self, msg):
        popup = ErrorPopup(self, message=msg)
        popup.exec()

    def calculate_click(self):
        mode = self.mode_box.currentText()
        left_text = self.left_edit.text()
        right_text = self.right_edit.text()
        n_text = self.n_edit.text()
        formula_text = self.formula_edit.toPlainText()

        if not validators.check_limits(left_text, right_text):
            self.show_error("Проверьте границы L и R (должно быть R > L).")
            return

        if not validators.is_positive_int(n_text):
            self.show_error("N должно быть целым числом больше 0.")
            return

        if not validators.check_mode(mode):
            self.show_error("Выбран неизвестный метод.")
            return

        try:
            func = validators.build_function(formula_text)
            func(1)
        except Exception:
            self.show_error("Ошибка в записи функции f(x).")
            return

        left = float(left_text)
        right = float(right_text)
        count = int(n_text)

        total, x_vals, y_vals, bar_x, bar_align, step = calc_integral(func, left, right, count, mode)
        img = make_plot_image(func, left, right, count, mode, total, x_vals, y_vals, bar_x, bar_align, step)

        qt_img = ImageQt(img)
        self.pic_label.setPixmap(QPixmap.fromImage(qt_img))
        self.result_lbl.setText("Ответ: " + str(round(total, 5)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = IntegralApp()
    win.show()
    sys.exit(app.exec())