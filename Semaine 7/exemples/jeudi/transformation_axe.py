from PySide6.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout
from PySide6.QtGui import QPainter, QPen, QTransform, QPixmap, QColorConstants, QFont, QBrush
from PySide6.QtCore import QPoint, QSize, QRect, Qt


class DessinTransform(QFrame):

    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.libelle_canevas = QLabel()
        self.disposition.addWidget(self.libelle_canevas)

        self.canevas = QPixmap(QSize(600, 600))
        self.canevas.fill(QColorConstants.White)

        painter = QPainter(self.canevas)
        crayon = QPen()
        crayon.setColor(QColorConstants.DarkBlue)
        painter.setPen(crayon)
        police = QFont()
        police.setFamily("Times")
        police.setPointSize(20)
        painter.setFont(police)

        brosse = QBrush()
        brosse.setStyle(Qt.BrushStyle.Dense2Pattern)
        painter.fillRect(QRect(300, 400, 20, 20), brosse)

        transform_texte = QTransform()
        transform_texte.translate(50, 50)
        transform_texte.rotate(45)
        painter.setTransform(transform_texte)
        painter.drawText(QPoint(0, 0), "Bonjour le monde!")

        transform_formes = QTransform()
        transform_formes.translate(100, 100)
        painter.setTransform(transform_formes)
        painter.drawArc(QRect(0, 0, 200, 200), 30 * 16, 120 * 16)

        transform_ellipse = QTransform()
        transform_ellipse.translate(300, 300)
        transform_ellipse.scale(10, 10)

        crayon_formes = QPen()
        crayon_formes.setColor(QColorConstants.Red)
        brosse_formes = QBrush()
        brosse_formes.setColor(QColorConstants.Red)
        brosse_formes.setStyle(Qt.BrushStyle.Dense6Pattern)
        crayon_formes.setBrush(brosse_formes)
        # painter.setTransform(transform_ellipse)
        # painter.setPen(crayon_formes)
        painter.setTransform(QTransform())
        painter.drawEllipse(QPoint(300, 300), 25, 35)

        painter.end()
        self.libelle_canevas.setPixmap(self.canevas)


app = QApplication()
dt = DessinTransform()
dt.show()
app.exec()

