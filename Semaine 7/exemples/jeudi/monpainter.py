from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QColorDialog, QFontDialog, QFrame, \
    QPushButton
from PySide6.QtGui import QPixmap, QPen, QPainter, QBrush, QColor, QColorConstants
from PySide6.QtCore import QSize, QPointF, Qt


class MonPainter(QFrame):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon Peintre 2025")
        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.libelle_canevas = QLabel()
        self.disposition_principale.addWidget(self.libelle_canevas)

        self.canevas = QPixmap(QSize(800, 600))
        self.canevas.fill(QColorConstants.White)
        self.libelle_canevas.setPixmap(self.canevas)

        self.disposition_couleurs = QHBoxLayout()
        self.disposition_principale.addLayout(self.disposition_couleurs)

        self.LISTE_COULEURS = ["#4cc23a", "#bd3c89", "#db1a37", "#eded21", "#000000"]

        # Modèle
        self.painter = QPainter()
        self.crayon = QPen()
        self.couleur_crayon = QColor("#644482")
        self.police = self.painter.font()
        self.position_debut = None

        for i in self.LISTE_COULEURS:
            bouton_couleur = BoutonCouleur(couleur=i, crayon=self.crayon)
            self.disposition_couleurs.addWidget(bouton_couleur)

    def mouseMoveEvent(self, event, /):
        # S'il y aucune postion de début, c'est un nouveau "dessin", on l'assigne à la position o`la souris a été clicked
        if self.position_debut is None:
            self.position_debut = event.localPos()

    def mouseReleaseEvent(self, event, /):
        position = event.localPos()
        self.dessiner_ligne(position)
        print(f"mouseReleaseEvent {position}")
        self.position_debut = None

    def dessiner_ligne(self, position_fin):
        painter = QPainter(self.canevas)
        painter.setPen(self.crayon)
        print(f"drawLine début:{self.position_debut} fin: {position_fin}")
        painter.drawLine(self.position_debut, position_fin)
        painter.end()
        self.libelle_canevas.setPixmap(self.canevas)


class BoutonCouleur(QPushButton):

    def __init__(self, couleur: str, crayon: QPen):
        super().__init__()
        self.setFixedSize(QSize(32, 32))
        self.setStyleSheet("background-color: " + couleur + ";")
        self.couleur = QColor(couleur)
        # self.clicked.connect(self.bouton_couleur_clicked)
        self.clicked.connect(lambda: self.crayon.setColor(self.couleur))
        self.crayon = crayon


app = QApplication()
mp = MonPainter()
mp.show()
app.exec()
