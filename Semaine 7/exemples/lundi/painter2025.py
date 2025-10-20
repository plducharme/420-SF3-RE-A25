from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QFrame, QVBoxLayout, QToolBar
from PySide6.QtGui import QPainter, QPen, QBrush, QPixmap, QVector2DList, QColor
from PySide6.QtCore import Qt, QSize, QPoint, QPointF

import random


class Painter2025(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()

        barre_couleurs = QToolBar()
        liste_couleurs = ["#3645b5", "#195c1f", "#8f891d", "#3cb8ba"]
        self.couleur_courante = "#000000"

        for couleur in liste_couleurs:
            bouton = QPushButton()
            bouton.setStyleSheet("background-color:" + couleur + ";")
            bouton.clicked.connect(lambda checked=False, c=couleur: self.changer_couleur(c))
            barre_couleurs.addWidget(bouton)

        self.libelle_canevas = QLabel()
        self.canevas = QPixmap(QSize(500, 500))
        self.canevas.fill(QColor("#FFFFFF"))
        self.libelle_canevas.setPixmap(self.canevas)

        disposition.addWidget(barre_couleurs)
        disposition.addWidget(self.libelle_canevas)
        self.setLayout(disposition)

    def changer_couleur(self, couleur: str):
        print(f"couleur clicked: {couleur}")
        self.couleur_courante = couleur

    def mouseMoveEvent(self, event, /):
        canevas = self.canevas
        painter = QPainter(canevas)
        crayon = QPen()
        crayon.setColor(self.couleur_courante)
        painter.setPen(crayon)

        position = event.position()
        # painter.drawPoint(position.toPoint())
        for i in range(1000):
            valeur_gauss_x = random.gauss(0, 10)
            valeur_gauss_y = random.gauss(0, 10)
            painter.drawPoint(QPointF(position.x() + valeur_gauss_x, position.y() + valeur_gauss_y))

        painter.end()
        self.libelle_canevas.setPixmap(canevas)


app = QApplication()
p = Painter2025()
p.show()
app.exec()







