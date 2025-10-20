# Exemple pour utiliser matplotlib avec PySide

from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

# indique à matplotlib de dessiner dans PySide au lieu de la fenêtre de console
matplotlib.use("Qt5Agg")


class PysideMatplotlib(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple Matplotlib widget")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        # Ajoute le widget (FigureCanvasQTAgg) pouvant contenir les graphiques matplotlib
        self.figure_canvas = FigureCanvasQTAgg()
        disposition.addWidget(self.figure_canvas)

        # Ajoute la barre d'outils de matplotlib et on l'assigne à notre Canevas
        self.barre_outils_mpl = NavigationToolbar2QT(self.figure_canvas, self.figure_canvas)

        # On se fait un graphique
        # Créer une figure
        self.figure = plt.figure()
        # Ajouter une droite
        coords_x = range(10)
        coords_y = [x**2 for x in coords_x]
        plt.plot(coords_x, coords_y, "b--")
        plt.title("Carrés de x")
        plt.legend(["y = x**2"])
        plt.xlabel("x")
        plt.ylabel("y")

        # Assigne la figure créée au widget de type FigureCanvasQTAgg, on aurait pu aussi réutiliser la figure générée
        # par défaut par le FigureCanvasQTAgg et la modifier à la place
        self.figure_canvas.figure = self.figure

        # Dessine le graphique, on utilise pas .show() mais .draw()
        self.figure_canvas.draw()


app = QApplication()
pm = PysideMatplotlib()
pm.show()
app.exec()






