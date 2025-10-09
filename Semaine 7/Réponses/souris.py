import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QColorDialog, QToolBar
from PySide6.QtGui import QColorConstants, QMouseEvent, QPainter, QPixmap, QPen
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.qcd = QColorDialog()
        self.couleur = QColorConstants.Black

        self.bouton_couleur = QPushButton("Couleur")
        self.barre_outils = QToolBar("Barre d'outils")
        self.barre_outils.addWidget(self.bouton_couleur)
        # TODO: À corriger, lorsque l'on ajoute la barre d'outils, les coordonnées sont décalées de la largeur de la barre
        # self.addToolBar(self.barre_outils)

        self.bouton_couleur.clicked.connect(self.changer_couleur)

        self.precedent_x, self.precedent_y = None, None

    # Pour éviter d'avoir des lignes "brisées", on dessine des lignes entre 2 points au lieu de plusieurs points
    def mouseMoveEvent(self, e: QMouseEvent):
        position = e.position()
        # Premier événement doit assigner le premier point, donc, on ne le dessine pas
        if self.precedent_x is None:
            self.precedent_x = position.x()
            self.precedent_y = position.y()
            return

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        qpen = QPen()
        qpen.setColor(self.couleur)
        painter.setPen(qpen)
        painter.drawLine(self.precedent_x, self.precedent_y, position.x(), position.y())
        painter.end()
        self.label.setPixmap(canvas)

        # Les coordonnées courantes deviennent les précédentes pour le prochain dessin
        self.precedent_x = position.x()
        self.precedent_y = position.y()

    def mouseReleaseEvent(self, e):
        self.precedent_x = None
        self.precedent_y = None

    def changer_couleur(self):
        self.qcd.exec()
        self.couleur = self.qcd.selectedColor()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()