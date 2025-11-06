from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem
from PySide6.QtCore import Qt, QTimer, QRect, QPointF, QSize
import random
import math


class Pong(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pong 2025")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.vue = QGraphicsView()
        self.vue.setMinimumSize(QSize(825, 625))
        self.disposition.addWidget(self.vue)
        self.jeu = PongJeu()
        self.vue.setScene(self.jeu.scene)

        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.mise_a_jour_jeu)
        self.timer.start()

    def mise_a_jour_jeu(self):
        self.jeu.mise_a_jour()
        self.jeu.verifier_collision()

    def keyPressEvent(self, event, /):

        if event.key() == Qt.Key.Key_W:
            self.jeu.bouger_palette(True, True)
        elif event.key() == Qt.Key.Key_S:
            self.jeu.bouger_palette(True, False)
        elif event.key() == Qt.Key.Key_I:
            self.jeu.bouger_palette(False, True)
        elif event.key() == Qt.Key.Key_K:
            self.jeu.bouger_palette(False, False)
        else:
            super().keyPressEvent(event)


class PongJeu:

    LARGEUR_JEU = 800
    HAUTEUR_JEU = 600

    LARGEUR_MUR = 20

    LARGEUR_PALETTE = 10
    LONGUEUR_PALETTE = 50
    DEPLACEMENT_PALETTE = 20

    ESPACEMENT = 20

    GRANDEUR_BALLE = 10
    VITESSE_BALLE = 200

    def __init__(self):

        self.score_j1 = 0
        self.score_j2 = 0
        self.scene = QGraphicsScene(QRect(0, 0, PongJeu.LARGEUR_JEU, PongJeu.HAUTEUR_JEU))

        self.palette_j1 = QGraphicsRectItem(QRect(0, 0, PongJeu.LARGEUR_PALETTE, PongJeu.LONGUEUR_PALETTE))
        self.palette_j2 = QGraphicsRectItem(QRect(0, 0, PongJeu.LARGEUR_PALETTE, PongJeu.LONGUEUR_PALETTE))

        position_depart_palette_j1 = QPointF(PongJeu.LARGEUR_MUR + PongJeu.ESPACEMENT, (PongJeu.HAUTEUR_JEU - 2 * PongJeu.LARGEUR_MUR - PongJeu.LONGUEUR_PALETTE) / 2)
        position_depart_palette_j2 = QPointF(PongJeu.LARGEUR_JEU - (PongJeu.LARGEUR_MUR + PongJeu.ESPACEMENT), (PongJeu.HAUTEUR_JEU - 2 * PongJeu.LARGEUR_MUR - PongJeu.LONGUEUR_PALETTE) / 2)

        self.palette_j1.setPos(position_depart_palette_j1)
        self.palette_j2.setPos(position_depart_palette_j2)
        self.scene.addItem(self.palette_j1)
        self.scene.addItem(self.palette_j2)

        self.mur_gauche = QGraphicsRectItem(QRect(0, 0, PongJeu.LARGEUR_MUR, PongJeu.HAUTEUR_JEU))
        self.mur_droit = QGraphicsRectItem(QRect(PongJeu.LARGEUR_JEU - PongJeu.LARGEUR_MUR, 0, PongJeu.LARGEUR_MUR, PongJeu.HAUTEUR_JEU))
        self.mur_haut = QGraphicsRectItem(QRect(0, 0, PongJeu.LARGEUR_JEU, PongJeu.LARGEUR_MUR))
        self.mur_bas = QGraphicsRectItem(QRect(0, PongJeu.HAUTEUR_JEU - PongJeu.LARGEUR_MUR, PongJeu.LARGEUR_JEU, PongJeu.LARGEUR_MUR))

        self.scene.addItem(self.mur_gauche)
        self.scene.addItem(self.mur_droit)
        self.scene.addItem(self.mur_haut)
        self.scene.addItem(self.mur_bas)

        self.text_score_j1 = QGraphicsTextItem(str(self.score_j1))
        self.text_score_j2 = QGraphicsTextItem(str(self.score_j2))
        self.text_score_j1.setPos(QPointF(50, 50))
        self.text_score_j2.setPos(QPointF(750, 50))

        self.scene.addItem(self.text_score_j1)
        self.scene.addItem(self.text_score_j2)

        self.balle = QGraphicsEllipseItem(QRect(0, 0, PongJeu.GRANDEUR_BALLE, PongJeu.GRANDEUR_BALLE))
        self.direction_balle = None
        self.generer_position_balle()

        self.scene.addItem(self.balle)

    def mise_a_jour(self):
        position_actuelle = self.balle.pos()
        nouvelle_position = QPointF(position_actuelle.x() + math.cos(math.radians(self.direction_balle) * PongJeu.VITESSE_BALLE), position_actuelle.y() + math.sin(math.radians(self.direction_balle)) * PongJeu.VITESSE_BALLE)
        if nouvelle_position.x() < 0:
            nouvelle_position.setX(0)
        elif nouvelle_position.x() > PongJeu.LARGEUR_JEU:
            nouvelle_position.setX(PongJeu.LARGEUR_JEU)
        elif nouvelle_position.y() < 0:
            nouvelle_position.setY(0)
        elif nouvelle_position.y() > PongJeu.HAUTEUR_JEU - PongJeu.LARGEUR_MUR:
            nouvelle_position.setY(PongJeu.HAUTEUR_JEU - PongJeu.LARGEUR_MUR)

        print(nouvelle_position, self.direction_balle)
        self.balle.setPos(nouvelle_position)

    def generer_position_balle(self):
        self.direction_balle = random.randint(-45, 45)
        gauche_droite = random.randint(0, 1)
        if gauche_droite == 0:
            self.direction_balle = -self.direction_balle
        print(f"direction balle: {self.direction_balle}")
        self.balle.setPos(QPointF(PongJeu.LARGEUR_JEU / 2, PongJeu.HAUTEUR_JEU / 2))

    def verifier_collision(self):
        liste_collisions = self.balle.collidingItems()

        for item in liste_collisions:
            if item == self.mur_gauche:
                self.score_j2 += 1
                self.text_score_j2.setPlainText(str(self.score_j2))
                self.generer_position_balle()
            elif item == self.mur_droit:
                self.score_j1 += 1
                self.text_score_j1.setPlainText(str(self.score_j1))
                self.generer_position_balle()
            elif item == self.mur_haut or item == self.mur_bas:
                self.direction_balle = -self.direction_balle
            elif item == self.palette_j1 or item == self.palette_j2:
                self.direction_balle = -self.direction_balle
            else:
                continue

    def bouger_palette(self, joueur_1: bool, direction_haut: bool):
        if joueur_1:
            if direction_haut:
                nouvelle_position = QPointF(self.palette_j1.pos().x(), self.palette_j1.pos().y() - PongJeu.DEPLACEMENT_PALETTE)
                if nouvelle_position.y() < 0:
                    nouvelle_position.setY(0)
                self.palette_j1.setPos(nouvelle_position)
            else:
                nouvelle_position = QPointF(self.palette_j1.pos().x(),
                                            self.palette_j1.pos().y() + PongJeu.DEPLACEMENT_PALETTE)
                if nouvelle_position.y() + PongJeu.LONGUEUR_PALETTE > PongJeu.HAUTEUR_JEU:
                    nouvelle_position.setY(PongJeu.HAUTEUR_JEU - PongJeu.LONGUEUR_PALETTE)
                self.palette_j1.setPos(nouvelle_position)
        else:
            if direction_haut:
                nouvelle_position = QPointF(self.palette_j2.pos().x(), self.palette_j2.pos().y() - PongJeu.DEPLACEMENT_PALETTE)
                if nouvelle_position.y() < 0:
                    nouvelle_position.setY(0)
                self.palette_j2.setPos(nouvelle_position)
            else:
                nouvelle_position = QPointF(self.palette_j2.pos().x(),
                                            self.palette_j2.pos().y() + PongJeu.DEPLACEMENT_PALETTE)
                if nouvelle_position.y() + PongJeu.LONGUEUR_PALETTE > PongJeu.HAUTEUR_JEU:
                    nouvelle_position.setY(PongJeu.HAUTEUR_JEU - PongJeu.LONGUEUR_PALETTE)
                self.palette_j2.setPos(nouvelle_position)


app = QApplication()
p = Pong()
p.show()
app.exec()




