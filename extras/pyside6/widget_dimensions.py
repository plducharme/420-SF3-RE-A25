from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QFrame


class WidgetDimensions(QMainWindow):
    def __init__(self):
        super().__init__()
        # Hérité de QMainWindow qui hérite de QWidget
        # Ceci va créer la fenêtre à la position (0,0) avec une largeur de 800 pixels et une hauteur de 600 pixels
        self.setGeometry(0, 0, 800, 600)

        # Par défaut, un widget va prendre toute la place disponible
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)

        libelle_defaut = QLabel("Par défaut")
        disposition.addWidget(libelle_defaut)

        libelle_restreint = QLabel("Restreint")
        # On va lui appliquer un style pour bien le distinguer
        libelle_restreint.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        # On définit une grandeur fixe. Si on agrandit, le widget ne va pas s'agrandir. de la même façon, le parent ne
        # pourra pas être réduit plus petit que la taille de ce widget.
        libelle_restreint.setFixedSize(QSize(200, 200))
        disposition.addWidget(libelle_restreint)


app = QApplication()
wd = WidgetDimensions()
wd.show()
app.exec()
