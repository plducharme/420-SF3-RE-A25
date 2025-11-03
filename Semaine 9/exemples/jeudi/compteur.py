from PySide6.QtWidgets import QApplication, QFrame, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap, QIcon, QMouseEvent
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT


class Compteur(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compteur Signal")
        # self.icone = QPixmap("./images/counter.png")
        self.setWindowIcon(QIcon("./images/counter.png"))

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.compteur = 0

        self.figure_canvas = FigureCanvasQTAgg()
        self.disposition.addWidget(self.figure_canvas)
        self.barre_outils = NavigationToolbar2QT(self.figure_canvas, self.figure_canvas)

        self.label_edit_valeur_increment = QLabel("Valeur d'incrémentation")
        self.edit_valeur_increment = QLineEdit()
        self.edit_valeur_increment.setText("3")
        self.edit_valeur_increment.textChanged.connect(self.update_valeur_increment)
        self.disposition_valeur = QHBoxLayout()
        self.disposition_valeur.addWidget(self.label_edit_valeur_increment)
        self.disposition_valeur.addWidget(self.edit_valeur_increment)
        self.disposition.addLayout(self.disposition_valeur)

        self.bouton_emit = BoutonEmit("Émettre Signal")
        self.bouton_emit.setEnabled(False)
        self.disposition.addWidget(self.bouton_emit)
        self.bouton_emit.incremente.connect(self.update_compteur)
        self.bouton_emit.valeur_increment = float(self.edit_valeur_increment.text())

    def update_valeur_increment(self, text: str):
        if len(text) == 0:
            if text[0] == "-" or text[0] == "+":
                return
        self.bouton_emit.valeur_increment = float(text)

    def update_compteur(self, valeur):
        self.compteur += valeur

        figure_mpl = plt.figure()
        plt.bar(1, self.compteur)
        # plt.legend()
        plt.xlabel("Compteur")
        plt.ylabel("Valeur")
        plt.ylim(0, 150)
        plt.title("Notre compteur de signal")
        self.figure_canvas.figure = figure_mpl
        self.figure_canvas.draw()

    def mousePressEvent(self, event: QMouseEvent, /):

        if event.button() == Qt.MouseButton.RightButton:
            self.bouton_emit.click()
        else:
            super().mousePressEvent(event)


class BoutonEmit(QPushButton):

    incremente = Signal(int)

    def __init__(self, texte):
        super().__init__(texte)
        self.valeur_increment = 1

    def click(self, /):
        super().click()
        self.incremente.emit(self.valeur_increment)


if __name__ == "__main__":
    app = QApplication()
    c = Compteur()
    c.show()
    app.exec()


