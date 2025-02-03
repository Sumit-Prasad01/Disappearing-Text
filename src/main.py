import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel

class TypingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Typing Word Counter")
        self.setGeometry(400, 400, 900, 700)
        self.setStyleSheet("background-color: #f0f8ff;")

        self.layout = QVBoxLayout()

        self.word_count_label = QLabel("Words typed: 0")
        self.word_count_label.setStyleSheet("font-size: 18px; color: #FF6347; font-weight: bold;")
        self.layout.addWidget(self.word_count_label)

        self.text_edit = QTextEdit(self)
        self.text_edit.setStyleSheet("""
            background-color: #fffacd;
            border: 2px solid #FF6347;
            font-size: 16px;
            padding: 10px;
            color: #2F4F4F;
        """)
        self.text_edit.setPlaceholderText("Start typing here...")
        self.layout.addWidget(self.text_edit)

        self.text_edit.textChanged.connect(self.count_words)

        self.timer = QTimer(self)
        self.timer.setInterval(5000)  # 5 seconds
        self.timer.timeout.connect(self.clear_text)

        self.setLayout(self.layout)

    def count_words(self):
        text = self.text_edit.toPlainText()
        words = [word for word in text.split() if word.strip()]
        word_count = len(words)
        self.word_count_label.setText(f"Words typed: {word_count}")

        if self.timer.isActive():
            self.timer.stop()

        self.timer.start()  # Restart the timer on each keypress

    def clear_text(self):
        self.text_edit.clear()
        self.word_count_label.setText("Words typed: 0")
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TypingApp()
    window.show()

    sys.exit(app.exec_())
