from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFrame, QHBoxLayout
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QTransform
from PySide6.QtCore import QSize, QPointF, QTimer, Qt, QRect, QPoint
import random


class Bombardier(QFrame):

    LARGEUR = 800
    HAUTEUR = 800

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bombardier 3000")

        self.libelle_canevas = QLabel()
        self.canevas = QPixmap(QSize(Bombardier.LARGEUR, Bombardier.HAUTEUR))
        self.canevas.fill(QColor(0, 0, 255))
        self.libelle_canevas.setPixmap(self.canevas)

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)
        self.disposition_principale.addWidget(self.libelle_canevas)

        self.disposition_controles = QHBoxLayout()
        self.bouton_demarrer = QPushButton("Démarrer")
        self.bouton_demarrer.clicked.connect(self.bouton_demarrer_clicked)
        self.disposition_controles.addWidget(self.bouton_demarrer)
        self.disposition_principale.addLayout(self.disposition_controles)

        self.jeu = BombardierJeu(Bombardier.LARGEUR, Bombardier.HAUTEUR)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.timer = QTimer(interval=100)
        self.timer.timeout.connect(self.boucle_jeu)
        self.timer.start()

    def boucle_jeu(self):

        match self.jeu.etat:
            case 1:
                return
            case 2:
                self.jeu.calculer_deplacements()
                self.jeu.dessiner(self.canevas)
                self.libelle_canevas.setPixmap(self.canevas)
                self.jeu.verifier_collision()
            case 3:
                return

    def keyPressEvent(self, event, /):
        if event.key() == Qt.Key.Key_B:
            if self.jeu.position_bombe is None:
                self.jeu.creer_bombe()
                print("Bomb!!!!!")
        super().keyPressEvent(event)

    def bouton_demarrer_clicked(self):
        self.jeu.etat = 2


class BombardierJeu:

    def __init__(self, largeur: int, hauteur: int):
        self.position_bombardier = QPoint(10, 50)
        self.vitesse = random.randint(5, 15)
        self.position_bombe = None
        self.position_cible = QPointF(random.randint(int(largeur / 2 - 50), int(largeur / 2 + 50)), 924)
        self.image_avion = QPixmap("./images/airplane.png")
        # self.image_avion = self.image_avion.scaled(QSize(32, 32), aspectMode=Qt.AspectRatioMode.KeepAspectRatio, mode=Qt.TransformationMode.SmoothTransformation)
        self.image_cible = QPixmap("./images/target.png")
        # self.image_cible = self.image_cible.scaled(QSize(32, 32))
        self.image_bombe = QPixmap("./images/nuclear-bomb.png")
        # self.image_bombe = self.image_bombe.scaled(QSize(16, 16))
        # 1 = Non débuté, 2 = En cours, 3 = Terminé
        self.etat = 1

    def dessiner(self, canevas: QPixmap):
        canevas.fill(QColor(0, 0, 255))
        painter = QPainter(canevas)

        transform = QTransform()
        transform.translate(self.position_bombardier.x(), self.position_bombardier.y())
        painter.setTransform(transform)
        painter.drawPixmap(QRect(0, 0, 32, 32), self.image_avion)

        transform_cible = QTransform()
        transform_cible.translate(self.position_cible.x(), self.position_cible.y())
        painter.setTransform(transform_cible)
        painter.drawPixmap(0, 0, self.image_cible)

        if self.position_bombe is not None:
            painter.drawPixmap(self.position_bombe.toPoint(), self.image_bombe)

        painter.end()

    def calculer_deplacements(self):
        self.position_bombardier = QPointF(self.position_bombardier.x() + self.vitesse, self.position_bombardier.y())
        if self.position_bombe is not None:
            self.position_bombe = QPointF(self.position_bombe.x() + self.vitesse, self.position_bombe + 10)

    def verifier_collision(self):
        pass

    def creer_bombe(self):
        self.position_bombe = self.position_bombardier


app = QApplication()
bomb = Bombardier()
bomb.show()
app.exec()
