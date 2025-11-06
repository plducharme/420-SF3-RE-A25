import random

from PySide6.QtGui import QBrush, QColor, QFont, QPainterPath
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QComboBox, QGraphicsRectItem, \
    QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsItemGroup, QGraphicsPixmapItem, QGraphicsPathItem, \
    QGraphicsSimpleTextItem, QFrame, QVBoxLayout
from PySide6.QtCore import QRect, QPoint, QSize, QTimer


class ExempleQGraphics(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple d'utilisations de QGraphicsItem")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.vue_haut = QGraphicsView()
        self.vue_bas = QGraphicsView()
        self.combo_scenes = QComboBox()

        self.disposition.addWidget(self.vue_haut)
        self.disposition.addWidget(self.vue_bas)
        self.disposition.addWidget(self.combo_scenes)

        self.scene_haut = QGraphicsScene(QRect(0, 0, 400, 400))
        self.vue_haut.setScene(self.scene_haut)

        # Ajoute les QGraphicsItems à la scene_haut
        self.g_rect = self.scene_haut.addRect(QRect(50, 60, 50, 75))
        self.brush_rect = QBrush()
        self.brush_rect.setColor(QColor(3, 86, 252))
        self.g_rect.setBrush(self.brush_rect)

        self.g_text = self.scene_haut.addText("Vive les ornithorynques!")
        self.police = self.g_text.font()
        print(self.police.families())
        self.police.setFamily("courrier new")
        self.police.setPointSize(16)
        self.g_text.setPos(QPoint(125, 125))
        self.g_text.setHtml('<a style="color: red;" href="https://fr.wikipedia.org/wiki/Ornithorynque">Vive les ornithorynques!</a>')

        self.g_text_simple = self.scene_haut.addSimpleText("Allo le monde!")
        self.g_text_simple.setPos(QPoint(45, 150))

        # Ajouter à la scene bas 1
        self.scene_bas_1 = QGraphicsScene(QRect(0, 0, 400, 400))
        self.vue_bas.setScene(self.scene_bas_1)
        self.combo_scenes.addItem("Scene Bas 1", self.scene_bas_1)

        self.painter_path = QPainterPath()
        self.painter_path.lineTo(QPoint(20, 20))
        self.painter_path.lineTo(QPoint(30, 45))
        self.painter_path.arcTo(QRect(30, 45, 50, 50), 15, 50)
        self.painter_path.closeSubpath()

        self.g_path_item = QGraphicsPathItem(self.painter_path)
        self.scene_bas_1.addItem(self.g_path_item)

        # Ajouter à scene 2
        self.group_items = QGraphicsItemGroup()
        self.group_items.addToGroup(QGraphicsRectItem(QRect(0, 0, 75, 75)))
        self.g_simple_texte_groupe = QGraphicsSimpleTextItem("Texte du groupe")
        self.g_simple_texte_groupe.setPos(QPoint(86, 35))
        self.group_items.addToGroup(self.g_simple_texte_groupe)
        self.scene_bas_2 = QGraphicsScene(QRect(0, 0, 400, 400))
        self.scene_bas_2.addItem(self.group_items)
        self.combo_scenes.addItem("Scene Bas 2", self.scene_bas_2)

        self.combo_scenes.currentIndexChanged.connect(self.combo_scene_changer_scene)

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start()

    def combo_scene_changer_scene(self, index):
        self.vue_bas.setScene(self.combo_scenes.currentData())

    def update_timer(self):
        print("Update timer")
        self.group_items.setPos(QPoint(int(self.group_items.x()) + random.randint(-20, 20), int(self.group_items.y())))


app = QApplication()
eqg = ExempleQGraphics()
eqg.show()
app.exec()
