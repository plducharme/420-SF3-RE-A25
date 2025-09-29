from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QFileDialog, QFrame, QPushButton, QMenu, QProgressBar, \
    QToolBar, QApplication, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QAction, QIcon
from element_tableau import ElementTableauPeriodique


class TableauPeriodique(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Élements du tableau périodique")
        self.setWindowIcon(QIcon("./images/chemistry.png"))

        cadre_principal = QFrame()
        self.setCentralWidget(cadre_principal)

        # Menu
        self.barre_menu = self.menuBar()

        # Menu Fichier
        self.menu_fichier = QMenu("&Fichier")
        self.barre_menu.addMenu(self.menu_fichier)

        self.action_ouvrir = QAction("Ouvrir")
        self.action_ouvrir.setIcon(QIcon("./images/open-folder.png"))
        self.action_ouvrir.triggered.connect(self.action_ourvrir_triggered)

        self.action_enregistrer = QAction("Enregistrer")
        self.action_enregistrer.setIcon(QIcon("./images/diskette.png"))

        self.action_quitter = QAction("Quitter")
        self.menu_fichier.addAction(self.action_ouvrir)
        self.menu_fichier.addAction(self.action_enregistrer)
        self.menu_fichier.addSeparator()
        self.menu_fichier.addAction(self.action_quitter)

        # Menu À propos
        self.menu_a_propos = QMenu("À propos")
        self.barre_menu.addMenu(self.menu_a_propos)
        self.action_a_propos = QAction("À propos")
        self.menu_a_propos.addAction(self.action_a_propos)

        # Barre d'outils
        self.barre_outils = QToolBar()
        self.barre_outils.addAction(self.action_ouvrir)
        self.barre_outils.addAction(self.action_enregistrer)
        self.addToolBar(self.barre_outils)

        # Disposition principale
        disposition_principale = QVBoxLayout()
        cadre_principal.setLayout(disposition_principale)

        self.libelle_nom = QLabel("N/D")
        police_nom = self.libelle_nom.font()
        police_nom.setBold(True)
        police_nom.setPointSize(20)
        self.libelle_nom.setFont(police_nom)
        disposition_principale.addWidget(self.libelle_nom)

        self.libelle_symbole = QLabel("Symbole:")
        self.symbole_edit = QLineEdit()
        disposition_symbole = QHBoxLayout()
        disposition_symbole.addWidget(self.libelle_symbole)
        disposition_symbole.addWidget(self.symbole_edit)
        disposition_principale.addLayout(disposition_symbole)

        self.libelle_numero_atomique = QLabel("Numéro Atomique:")
        self.numero_edit = QLineEdit()
        disposition_numero_atomique = QHBoxLayout()
        disposition_numero_atomique.addWidget(self.libelle_numero_atomique)
        disposition_numero_atomique.addWidget(self.numero_edit)
        disposition_principale.addLayout(disposition_numero_atomique)



        # Modèle
        self.elements_tableau = None

    def action_ourvrir_triggered(self):
        chemin, filtre = QFileDialog.getOpenFileName(parent=self, caption="Ouvrir un CSV", dir=".", filter="Fichier CSV (*.csv)")
        if chemin:
            self.elements_tableau = ElementTableauPeriodique.charger_donnees(chemin)



app = QApplication()
tp = TableauPeriodique()
tp.show()
app.exec()




