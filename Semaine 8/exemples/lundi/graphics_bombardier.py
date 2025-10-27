from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFrame, QVBoxLayout, \
    QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPointF, QSize, QRectF, Qt, QTimer
import random


class BombardierApp(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bombardier 2025")
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.vue = QGraphicsView()
        self.scene = QGraphicsScene(QRectF(0, 0, 500, 500))
        self.vue.setScene(self.scene)

        self.bombardier = Bombardier(QPointF(10, 10))
        self.scene.addItem(self.bombardier)

        self.cible = Cible(QPointF(random.randint(200, 400), 400))
        self.scene.addItem(self.cible)
        # self.scene.addRect(QRectF(25, 25, 50, 50))

        self.bombe = None

        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.mise_a_jour_objets)
        self.timer.start()

        self.disposition.addWidget(self.vue)

    def mise_a_jour_objets(self):
        self.bombardier.bouger()
        if self.bombe is not None:
            self.bombe.bouger()
            print(self.bombe.collidesWithItem(self.cible, Qt.ItemSelectionMode.IntersectsItemShape))
            if self.bombe.collidesWithItem(self.cible, Qt.ItemSelectionMode.IntersectsItemShape):
                message_gagnant = QMessageBox()
                message_gagnant.setText("Vous avez gagné!")
                message_gagnant.setWindowTitle("Bravo!")
                message_gagnant.exec()
                self.scene.removeItem(self.bombe)
                self.bombe = None

    def keyPressEvent(self, event, /):

        if event.key() == Qt.Key.Key_B:
            if self.bombe is None:
                self.bombe = Bombe(self.bombardier.pos())
                self.scene.addItem(self.bombe)



class Bombardier(QGraphicsPixmapItem):

    def __init__(self, position: QPointF):
        super().__init__()
        pix = QPixmap("../images/airplane.png")
        pix = pix.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(pix)
        self.setPos(position)

    def bouger(self):
        self.setPos(QPointF(self.x() + 10, self.y()))


class Cible(QGraphicsPixmapItem):

    def __init__(self, position: QPointF):
        super().__init__()
        self.setPos(position)
        pix = QPixmap("../images/target.png").scaled(QSize(64, 64))
        self.setPixmap(pix)


class Bombe(QGraphicsPixmapItem):

    def __init__(self, position: QPointF):
        super().__init__()
        pix = QPixmap("../images/nuclear-bomb.png").scaled(QSize(32, 32))
        self.setPixmap(pix)
        self.setPos(position)

    def bouger(self):
        self.setPos(self.x() + 10, self.y() + 20)



app = QApplication()
ba = BombardierApp()
ba.show()
app.exec()
