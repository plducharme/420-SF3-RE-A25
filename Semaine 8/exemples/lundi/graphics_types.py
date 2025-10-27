import random

from PySide6.QtCore import QPointF, QSize, QRect, QPoint, Qt, QTimer, QLine
from PySide6.QtGui import QPixmap, QColorConstants, QBrush, QPolygon, QFontDatabase, QPen, QPainterPath
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QPushButton, QGraphicsItemGroup, \
    QGraphicsPixmapItem, QGraphicsTextItem


class GraphicsTypes(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Types de QGraphicsItem")

        self.brush_bleu = QBrush()
        self.brush_bleu.setColor(QColorConstants.Blue)
        self.brush_bleu.setStyle(Qt.BrushStyle.Dense1Pattern)

        self.brush_vert = QBrush()
        self.brush_vert.setColor(QColorConstants.Green)
        self.brush_vert.setStyle(Qt.BrushStyle.RadialGradientPattern)

        self.pen = QPen()
        self.pen.setWidth(5)
        self.pen.setBrush(self.brush_vert)
        self.pen.setStyle(Qt.PenStyle.SolidLine)
        self.pen.setColor(QColorConstants.DarkMagenta)

        self.scene = QGraphicsScene(QRect(0, 0, 500, 500), backgroundBrush=self.brush_vert)
        self.setScene(self.scene)

        gtexte = self.scene.addText("Vive les graphics!")
        gtexte.setPos(QPointF(10, 350))
        # On s'imprime la liste à la console pour voir les valeurs possibles, ne devrait pas être dans le code
        print(QFontDatabase.families())

        police = gtexte.font()
        police.setPointSize(24)

        police.setFamily("Algerian")
        gtexte.setFont(police)

        pix = QPixmap("../images/chat_0.png").scaled(QSize(64, 64))
        gpixmap = self.scene.addPixmap(pix)
        gpixmap.setPos(QPointF(10, 10))

        grect = self.scene.addRect(QRect(120, 120, 50, 50))
        grect.setBrush(self.brush_bleu)
        grect.setPen(self.pen)

        # l'ellipse est délimitée par son rectangle
        self.scene.addEllipse(QRect(325, 250, 50, 60))

        # On crée un polygone que l'on referme
        polygone = QPolygon()
        polygone.append(QPoint(60, 80))
        polygone.append(QPoint(70, 125))
        polygone.append(QPoint(50, 125))
        polygone.append(QPoint(60, 80))

        self.scene.addPolygon(polygone)

        # Ajoute un widget à une position spécifique
        self.bouton = self.scene.addWidget(QPushButton("Test"))
        self.bouton.setPos(QPointF(250, 250))

        # Un QPainterPath peut être utiliser pour dessiner un widget, entre autres
        # Dans un QPainterPath, les coordonnées sont "locales" au QPainterPath
        self.painter_path = QPainterPath()
        self.painter_path.addText(QPoint(10, 10), police, "Path")
        self.painter_path.addEllipse(QRect(0, 0, 50, 50))
        self.gpath = self.scene.addPath(self.painter_path)
        self.gpath.setPos(QPointF(325, 50))

        self.scene.addLine(QLine(200, 75, 250, 150), self.pen)

        # Les items d'un groupe ont leurs propres coordonnées dans la scene, le groupe permet d'appliquer une opération à tous les éléments du groupe
        self.groupe_items = QGraphicsItemGroup()
        self.pixmap_item = QGraphicsPixmapItem(pix)
        self.pixmap_item.setPos(QPointF(90, 90))
        self.groupe_items.addToGroup(self.pixmap_item)
        self.texte_item = QGraphicsTextItem("Texte Groupe")
        self.texte_item.setPos(QPointF(120, 120))
        self.groupe_items.addToGroup(self.texte_item)
        self.groupe_items.setPos(QPointF(0, 0))
        self.scene.addItem(self.groupe_items)

        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.bouger_items)

        self.timer.start()

    def bouger_items(self):
        self.bouger_path()
        self.bouger_groupe()

    # Tous les éléments du path vont bouger ensemble
    def bouger_path(self):
        self.gpath.setX(self.gpath.x() + random.randint(-10, 10))
        self.gpath.setY(self.gpath.y() + random.randint(-10, 10))

    def bouger_groupe(self):
        if self.groupe_items.x() < 500:
            self.groupe_items.setX(self.groupe_items.x() + 20)
        else:
            self.groupe_items.setX(0)


app = QApplication()
gt = GraphicsTypes()
gt.show()
app.exec()
