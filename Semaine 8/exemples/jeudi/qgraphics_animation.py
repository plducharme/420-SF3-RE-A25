from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QPointF, QVariantAnimation, QObject
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QComboBox, QGraphicsView, QGraphicsScene, QHBoxLayout, \
    QPushButton, QGraphicsEllipseItem, QGraphicsItem, QGraphicsWidget, QStyle, QGraphicsRectItem


class GraphicsAnimation(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation de QGraphics")

        disposition = QVBoxLayout()
        self.setLayout(disposition)
        disposition_controles = QHBoxLayout()

        self.easingcurve_courant = QEasingCurve.Type.Linear
        self.liste_easingcurves = QComboBox()
        self.creer_combo_easing()
        self.liste_easingcurves.currentIndexChanged.connect(self.liste_easingcurves_index_changed)
        disposition_controles.addWidget(self.liste_easingcurves)
        self.bouton_restart = QPushButton("Restart")
        self.bouton_restart.clicked.connect(self.bouton_restart_clicked)
        disposition_controles.addWidget(self.bouton_restart)

        disposition.addLayout(disposition_controles)

        self.graphics_view = QGraphicsView()
        self.graphics_scene = QGraphicsScene(0, 0, 400, 400)
        self.graphics_view.setScene(self.graphics_scene)

        self.graphics_ellipse = QGraphicsEllipseItem(10, 10, 50, 60)
        self.graphics_ellipse_animation = ItemAnimator(self.graphics_ellipse, QPointF(10, 10), QPointF(300, 250), 2000, self.easingcurve_courant, loop=False)

        self.graphics_scene.addItem(self.graphics_ellipse)

        # self.graphics_widget = QGraphicsWidget()
        # self.graphics_widget.setGraphicsItem(QGraphicsRectItem())
        # self.graphics_widget.setPos(QPointF(30, 30))
        #
        # self.graphics_widget_animation = QPropertyAnimation(self.graphics_widget, b"x")
        # self.graphics_widget_animation.setStartValue(30)
        # self.graphics_widget_animation.setEndValue(350)
        # self.graphics_widget_animation.setEasingCurve(self.easingcurve_courant)
        # self.graphics_scene.addItem(self.graphics_widget)

        disposition.addWidget(self.graphics_view)

    def bouton_restart_clicked(self):
        self.graphics_ellipse_animation.play()
        # self.graphics_widget_animation.start()

    def creer_combo_easing(self):
        self.liste_easingcurves.addItem("InBounce", QEasingCurve.Type.InBounce)
        self.liste_easingcurves.addItem("InOutElastic", QEasingCurve.Type.InOutElastic)
        self.liste_easingcurves.addItem("InOutSine", QEasingCurve.Type.InOutSine)

    def liste_easingcurves_index_changed(self):
        self.easingcurve_courant = self.liste_easingcurves.currentData()
        self.graphics_ellipse_animation.anim.setEasingCurve(self.easingcurve_courant)
        # self.graphics_widget_animation.setEasingCurve(self.easingcurve_courant)


class ItemAnimator(QObject):
    def __init__(self, item: QGraphicsItem, position_debut: QPointF, position_fin: QPointF,
                 duration: int = 2000, easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic, loop: bool = True):
        super().__init__()
        self.item = item
        self.debut = QPointF(position_debut)
        self.fin = QPointF(position_fin)
        self.anim = QVariantAnimation(self)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setDuration(duration)
        self.anim.setEasingCurve(QEasingCurve(easing))
        self.anim.valueChanged.connect(self._on_value)
        self.anim.setLoopCount(-1 if loop else 1)

    def _on_value(self, v):
        # interpolation manuelle entre debut et fin
        x = self.debut.x() + (self.fin.x() - self.debut.x()) * float(v)
        y = self.debut.y() + (self.fin.y() - self.debut.y()) * float(v)
        self.item.setPos(QPointF(x, y))

    def play(self):
        self.anim.start()

    def pause(self):
        if self.anim.state() == self.anim.State.Running:
            self.anim.pause()

    def resume(self):
        if self.anim.state() == self.anim.State.Paused:
            self.anim.resume()

    def stop(self):
        self.anim.stop()


app = QApplication()
ga = GraphicsAnimation()
ga.show()
app.exec()

