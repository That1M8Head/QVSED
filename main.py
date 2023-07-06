from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QPlainTextEdit, QLineEdit, QAction, QShortcut
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.uic import loadUi
import os

config_file = "config.py"

if not os.path.isfile(config_file):
    # Create the config file with default options
    with open(config_file, 'w') as f:
        f.write('''# Font
font_family = ["JetBrains Mono", "Cascadia Code", "Consolas", "Menlo", "monospace"]
font_size = 11

# Colours
# Yes, you have to use the British spellings
font_colour = "#FFFFFF"
foreground_colour = "#393F4A"
border_colour = "#31353F"
background_colour = "#282C34"
scrollbar_colour = "#393F4A"
''')
        
import config as qvsed_config

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("QVSED.ui", self)

        font = QFont()
        font.setFamilies(qvsed_config.font_family)
        font.setPointSize(qvsed_config.font_size)
        QApplication.instance().setFont(font)
        self.update_widget_fonts(self)

        text_area = self.findChild(QPlainTextEdit, "textArea")
        text_area.setFocus()

        self.findChild(QPushButton, "clearButton").clicked.connect(self.clear_button_clicked)
        self.findChild(QPushButton, "saveButton").clicked.connect(self.save_button_clicked)
        self.findChild(QPushButton, "openButton").clicked.connect(self.open_button_clicked)
        self.findChild(QPushButton, "helpButton").clicked.connect(self.help_button_clicked)
        self.findChild(QPushButton, "quitButton").clicked.connect(self.quit_button_clicked)

        self.clear_action = QAction("Clear Text", self)
        self.save_action = QAction("Save File", self)
        self.open_action = QAction("Open File", self)
        self.help_action = QAction("Get Help", self)
        self.quit_action = QAction("Quit QVSED", self)

        self.clear_shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.open_shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.help_shortcut = QShortcut(QKeySequence("Ctrl+H"), self)
        self.quit_shortcut = QShortcut(QKeySequence("Alt+Q"), self)

        self.clear_shortcut.activated.connect(self.clear_button_clicked)
        self.save_shortcut.activated.connect(self.save_button_clicked)
        self.open_shortcut.activated.connect(self.open_button_clicked)
        self.help_shortcut.activated.connect(self.help_button_clicked)
        self.quit_shortcut.activated.connect(self.quit_button_clicked)

    def clear_button_clicked(self):
        text_area = self.findChild(QPlainTextEdit, "textArea")
        
        if text_area.toPlainText() == "":
            self.echoArea_Update("Text Area is already blank.")
            return

        text_area.clear()

        self.echoArea_Update("Text Area has been cleared.")

    def save_button_clicked(self):
        text_area = self.findChild(QPlainTextEdit, "textArea")

        if text_area.toPlainText() == "":
            self.echoArea_Update("Text Area is blank, will not save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save File")

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(text_area.toPlainText())
                file_name = os.path.basename(file_path)
                self.echoArea_Update(f"Saved file {file_name}.")
            except Exception as e:
                self.echoArea_Update(f"Error saving file: {str(e)}")

    def open_button_clicked(self):
        text_area = self.findChild(QPlainTextEdit, "textArea")

        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text_area.setPlainText(file.read())
                file_name = os.path.basename(file_path)
                self.echoArea_Update(f"Opened file {file_name}.")
            except Exception as e:
                self.echoArea_Update(f"Error opening file: {str(e)}")

    def help_button_clicked(self):
        # Find the QPlainTextEdit widget by its object name
        text_area = self.findChild(QPlainTextEdit, "textArea")

        help_message = """QVSED - Qt-based Volatile Small Editor
========================================

QVSED is a volatile text editor, meaning that there are no restrictions against unsaved work or bad files, licensed under the GNU General Public License version 3 or later.

This is the Text Area, where the actual editing takes place. Type anything you want into here, and edit as you please.
Down there, below the Text Area is the Echo Area, where messages and errors will be displayed.
On the left of the QVSED window is the Action Deck, containing commands to clear the Text area, open or save a file, display this help text or quit QVSED.

I hope you enjoy using QVSED! I enjoyed writing it, and it's a nice little venture into my first Qt project.

- Arsalan Kazmi <sonicspeed848@gmail.com>, That1M8Head on GitHub"""

        self.echoArea_Update("Help message shown in Text Area.")

        text_area.setPlainText(help_message)

    def quit_button_clicked(self):
        QApplication.quit()

    def echoArea_Update(self, message):
        echo_area = self.findChild(QLineEdit, "echoArea")
        echo_area.setText(message)

    def update_widget_fonts(self, widget):
        if widget is None:
            return

        widget.setFont(QApplication.instance().font())

        for child_widget in widget.findChildren(QWidget):
            self.update_widget_fonts(child_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
