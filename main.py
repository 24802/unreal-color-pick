import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QColorDialog, QFrame, QSpacerItem, QSizePolicy, QLabel
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtCore import Qt
import ctypes

class CustomColorDialog(QColorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOption(QColorDialog.ColorDialogOption.NoButtons, True)
        self.setOption(QColorDialog.ColorDialogOption.DontUseNativeDialog, True)
        self.initUI()

    def initUI(self):
        for child in self.findChildren(QWidget):
            if 'qt_colorpatch' in child.objectName():
                child.setVisible(False)
        for child in self.findChildren(QLineEdit):
            child.setFixedWidth(100)

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()
        self.color_dialog = CustomColorDialog()
        self.color_dialog.currentColorChanged.connect(self.update_color_display)
        self.main_layout.addWidget(self.color_dialog)
        self.value_layout = QVBoxLayout()
        self.rgb_r = QLineEdit()
        self.rgb_g = QLineEdit()
        self.rgb_b = QLineEdit()
        self.hsb_h = QLineEdit()
        self.hsb_s = QLineEdit()
        self.hsb_v = QLineEdit()
        self.hex_val = QLineEdit()
        self.unreal_r = QLineEdit()
        self.unreal_g = QLineEdit()
        self.unreal_b = QLineEdit()
        self.add_label_and_textbox("R:", self.rgb_r)
        self.add_label_and_textbox("G:", self.rgb_g)
        self.add_label_and_textbox("B:", self.rgb_b)
        self.add_separator()
        self.add_label_and_textbox("H:", self.hsb_h)
        self.add_label_and_textbox("S:", self.hsb_s)
        self.add_label_and_textbox("V:", self.hsb_v)
        self.add_separator()
        self.add_label_and_textbox("HEX:", self.hex_val)
        self.add_separator()
        self.add_label_and_textbox("Unreal R:", self.unreal_r)
        self.add_label_and_textbox("Unreal G:", self.unreal_g)
        self.add_label_and_textbox("Unreal B:", self.unreal_b)
        self.rgb_r.textChanged.connect(self.update_color_from_text)
        self.rgb_g.textChanged.connect(self.update_color_from_text)
        self.rgb_b.textChanged.connect(self.update_color_from_text)
        self.hsb_h.textChanged.connect(self.update_color_from_text)
        self.hsb_s.textChanged.connect(self.update_color_from_text)
        self.hsb_v.textChanged.connect(self.update_color_from_text)
        self.hex_val.textChanged.connect(self.update_color_from_text)
        self.unreal_r.textChanged.connect(self.update_color_from_text)
        self.unreal_g.textChanged.connect(self.update_color_from_text)
        self.unreal_b.textChanged.connect(self.update_color_from_text)
        self.main_layout.addLayout(self.value_layout)
        self.setLayout(self.main_layout)
        self.setWindowTitle('Unreal Color Picker')
        self.show()

    def add_label_and_textbox(self, label_text, textbox):
        hbox = QHBoxLayout()
        label = QLabel(label_text)
        hbox.addWidget(label)
        hbox.addWidget(textbox)
        self.value_layout.addLayout(hbox)

    def add_separator(self):
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.value_layout.addItem(spacer)
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.value_layout.addWidget(line)
        self.value_layout.addItem(spacer)

    def update_color_display(self, color):
        r, g, b, _ = color.getRgb()
        h, s, v, _ = color.getHsv()
        hex_val = color.name()
        unreal_r = round(r / 255.0, 14)
        unreal_g = round(g / 255.0, 14)
        unreal_b = round(b / 255.0, 14)
        self.rgb_r.setText(str(r))
        self.rgb_g.setText(str(g))
        self.rgb_b.setText(str(b))
        self.hsb_h.setText(str(h))
        self.hsb_s.setText(str(s))
        self.hsb_v.setText(str(v))
        self.hex_val.setText(hex_val)
        self.unreal_r.setText(f"{unreal_r:.14f}")
        self.unreal_g.setText(f"{unreal_g:.14f}")
        self.unreal_b.setText(f"{unreal_b:.14f}")

    def update_color_from_text(self):
        try:
            r = int(self.rgb_r.text())
            g = int(self.rgb_g.text())
            b = int(self.rgb_b.text())
            color = QColor(r, g, b)
            self.color_dialog.setCurrentColor(color)
        except ValueError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))  # 창 아이콘 설정
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('myappid')  # 작업 표시줄 아이콘 설정
    ex = ColorPicker()
    sys.exit(app.exec())