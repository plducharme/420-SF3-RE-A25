from PySide6.QtWidgets import QApplication, QFrame, QWidget, QPushButton
from PySide6.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSize, QPointF, QEasingCurve


class AnimationWidgets(QFrame):

    def __init__(self):
        super().__init__()

        self.resize(QSize(800, 600))

        self.widget_generique = QWidget(self)
        self.widget_generique.setStyleSheet("background-color: #AAFF99;")

        self.bouton = QPushButton("Test", parent=self)

        self.animation_widget = QPropertyAnimation(self.widget_generique, b"size")
        self.animation_widget.setStartValue(QSize(50, 50))
        self.animation_widget.setEndValue(QSize(90, 120))
        self.animation_widget.setDuration(3000)
        self.animation_widget.setEasingCurve(QEasingCurve.Type.Linear)

        self.animation_bouton = QPropertyAnimation(self.bouton, b"pos")
        self.animation_bouton.setStartValue(QPointF(75, 75))
        self.animation_bouton.setEndValue(QPointF(10, 200))
        self.animation_bouton.setDuration(1500)
        self.animation_bouton.setEasingCurve(QEasingCurve.Type.InOutElastic)

        self.groupe_animation = QParallelAnimationGroup()
        self.groupe_animation.addAnimation(self.animation_widget)
        self.groupe_animation.addAnimation(self.animation_bouton)

        self.groupe_animation.start()


app = QApplication()
aw = AnimationWidgets()
aw.show()
app.exec()
