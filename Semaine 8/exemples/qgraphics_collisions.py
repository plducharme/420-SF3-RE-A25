from PySide6.QtWidgets import QApplication, QTextEdit, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPointF, QRectF, QSize, Qt

class GraphicsCollision(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple detection de collisions")
        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.vue = QGraphicsView()
        self.disposition.addWidget(self.vue)
        self.output = QTextEdit()
        self.disposition.addWidget(self.output)

        # Scene à (0,0) de grandeur 500 x 500
        self.scene = QGraphicsScene(QRectF(0, 0, 500, 500))
        self.vue.setScene(self.scene)

        self.robot_pix = QPixmap("./images/robot2.png")
        # On redimensionne le pixmap à 64 x 4 pixels en gardant les proportions
        self.robot_pix = self.robot_pix.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.item_robot1 = QGraphicsPixmapItem(self.robot_pix)
        self.item_robot1.setPos(QPointF(50, 50))

        self.item_robot2 = QGraphicsPixmapItem(self.robot_pix)
        self.item_robot2.setPos(QPointF(300, 300))

        self.mur_pix = QPixmap("./images/wall.png")
        self.mur_pix = self.mur_pix.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.item_mur = QGraphicsPixmapItem(self.mur_pix)
        self.item_mur.setPos(QPointF(310, 310))

        # On va se tenir un dictionnaire pour savoir ce qui entraine une collision
        self.items = {"mur": self.item_mur, "robot1": self.item_robot1, "robot2": self.item_robot2}

        # On ajoute tout à la scene
        for item in self.items.values():
            self.scene.addItem(item)

        # Regarde pour les collisions
        for nom, item in self.items.items():
            # collidingItems retourne la liste des items entrant en collision avec l'item sur lequel la méthode est appelée
            collisions = item.collidingItems(Qt.ItemSelectionMode.IntersectsItemShape)
            if len(collisions) > 0:
                # on va faire un output de ce qui collisionne
                for nom_obj_collision, obj_collision in self.items.items():
                    for collision in collisions:
                        if collision == obj_collision:
                            self.output.append(f"{nom} a détecté une collision avec {nom_obj_collision}")


app = QApplication()
gc = GraphicsCollision()
gc.show()
app.exec()







