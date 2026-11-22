APP_STYLE = """
QWidget {
    background-color: #f4f6f9;
    font-family: Arial, sans-serif;
    color: #222222;
}

QGroupBox {
    border: 1px solid #cccccc;
    border-radius: 6px;
    margin-top: 12px;
    padding: 10px;
    background-color: #ffffff;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #333333;
    font-weight: bold;
}

QLineEdit, QComboBox, QPlainTextEdit {
    background-color: #ffffff;
    border: 1px solid #bbbbbb;
    border-radius: 4px;
    padding: 4px;
    font-size: 13px;
}

QPushButton {
    background-color: #2b6cb0;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    font-weight: bold;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #2c5282;
}
"""

ERROR_STYLE = """
QDialog {
    background-color: #ffffff;
}

QLabel {
    color: #b91c1c;
    font-size: 14px;
}

QPushButton {
    background-color: #dc2626;
    color: #ffffff;
    border-radius: 4px;
    padding: 6px 14px;
}
"""