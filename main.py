import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


app = QApplication(sys.argv)

# Create Transparent window
window = QLabel()
window.setAttribute(Qt.WA_TranslucentBackground)
window.setWindowFlags(
    Qt.FramelessWindowHint |
    Qt.WindowStaysOnTopHint
)

# character
pixmap = QPixmap("assets/img1.png")
pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
window.setPixmap(pixmap)
window.resize(pixmap.size())

window.move(800,200)
window.show()

sys.exit(app.exec())