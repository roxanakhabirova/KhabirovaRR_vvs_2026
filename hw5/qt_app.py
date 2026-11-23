import sys
from PyQt6 import QtWidgets
from calc import DISCOUNTS, check_numbers, calc_discount


class DiscountWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор скидки (PyQt6)")
        self.resize(400, 300)

        layout = QtWidgets.QVBoxLayout()

        # Заголовок
        title = QtWidgets.QLabel("Расчёт цены со скидкой")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        # Поля ввода и выбор параметров
        form = QtWidgets.QFormLayout()

        self.price_input = QtWidgets.QLineEdit()
        self.count_input = QtWidgets.QLineEdit()

        self.card_box = QtWidgets.QComboBox()
        self.card_box.addItems(list(DISCOUNTS.keys()))

        self.promo_check = QtWidgets.QCheckBox("Есть промокод (+5%)")

        form.addRow("Цена за 1 шт (руб.):", self.price_input)
        form.addRow("Количество (шт.):", self.count_input)
        form.addRow("Карта клиента:", self.card_box)
        form.addRow(self.promo_check)
        layout.addLayout(form)

        # Кнопки
        btn_row = QtWidgets.QHBoxLayout()
        btn_calc = QtWidgets.QPushButton("Посчитать")
        btn_calc.clicked.connect(self.count_click)

        btn_clear = QtWidgets.QPushButton("Очистить")
        btn_clear.clicked.connect(self.clear_click)

        btn_row.addWidget(btn_calc)
        btn_row.addWidget(btn_clear)
        layout.addLayout(btn_row)

        # Вывод результата
        self.result_label = QtWidgets.QLabel("К оплате: —")
        self.result_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def count_click(self):
        ok, res = check_numbers(self.price_input.text(), self.count_input.text())
        if not ok:
            QtWidgets.QMessageBox.warning(self, "Ошибка", res)
            return

        price, count = res
        total, saved = calc_discount(price, count, self.card_box.currentText(), self.promo_check.isChecked())
        self.result_label.setText("К оплате: " + str(total) + " руб. (скидка " + str(saved) + " руб.)")

    def clear_click(self):
        self.price_input.clear()
        self.count_input.clear()
        self.card_box.setCurrentIndex(0)
        self.promo_check.setChecked(False)
        self.result_label.setText("К оплате: —")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = DiscountWindow()
    win.show()
    sys.exit(app.exec())