from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QPixmap, QColorConstants, QPen, QBrush
from PySide6.QtCore import QSize, Qt


class QPainterEx(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_centrale = QLabel()
        # Création d'un canevas d'une largeur de 500 pixels et d'une hauteur de 400 pixels
        canevas = QPixmap(QSize(500, 400))
        # Remplir le canevas d'une couleur
        canevas.fill(QColorConstants.White)

        self.etiquette_centrale.setPixmap(canevas)
        self.setCentralWidget(self.etiquette_centrale)

        self.dessiner()

    def dessiner(self):
        # Retrouver le pixmap pour notre canevas via notre QLabel
        canevas = self.etiquette_centrale.pixmap()
        painter = QPainter(canevas)
        crayon = QPen()
        crayon.setWidth(30)
        pinceau = QBrush()
        pinceau.setStyle(Qt.BrushStyle.Dense5Pattern)
        pinceau.setColor(QColorConstants.Red)
        crayon.setBrush(pinceau)
        painter.setPen(crayon)
        painter.drawLine(50, 50, 75, 100)
        crayon2 = QPen()
        crayon2.setColor(QColorConstants.DarkBlue)
        crayon2.setWidth(15)
        painter.setPen(crayon2)
        painter.drawPoint(200, 250)

        painter.end()
        self.etiquette_centrale.setPixmap(canevas)


app = QApplication()
qp = QPainterEx()
qp.show()
app.exec()