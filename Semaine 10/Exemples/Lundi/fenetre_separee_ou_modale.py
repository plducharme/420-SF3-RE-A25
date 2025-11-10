from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QVBoxLayout, QLabel, QPushButton, QFrame, QApplication
from PySide6.QtGui import QAction


class ExempleFenetres(QMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = QMenu("exemple")
        self.action_nouvelle_fenetre = QAction("Nouvelle Fenêtre", parent=self )
        self.action_nouvelle_fenetre.triggered.connect(self.action_fenetre_separee_triggered)
        self.action_modale = QAction("Modale", parent=self)
        self.action_modale.triggered.connect(self.action_modale_triggered)

        self.barre_menu = self.menuBar()
        self.barre_menu.addMenu(self.menu)
        self.menu.addAction(self.action_nouvelle_fenetre)
        self.menu.addAction(self.action_modale)

        self.fs = None

    def action_modale_triggered(self):
        dialogue = QDialog(parent=self)
        dialogue.setWindowTitle("Fenêtre Modale")
        layout = QVBoxLayout()
        label = QLabel("Fenêtre Modale")
        dialogue.setModal(True)
        layout.addWidget(label)
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(dialogue.close)
        layout.addWidget(bouton)
        dialogue.setLayout(layout)
        dialogue.exec()

    def action_fenetre_separee_triggered(self):
        self.fs = FenetreSeparee(self)
        self.fs.show()


class FenetreSeparee(QFrame):

    def __init__(self, parent):
        super().__init__()
        # self.setParent(parent)
        self.setWindowTitle("Fenêtre Séparée")
        self.layout = QVBoxLayout()
        self.label = QLabel("Fenêtre Séparée")
        self.bouton = QPushButton("Fermer")
        self.bouton.clicked.connect(self.close)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.bouton)
        self.setLayout(self.layout)


app = QApplication()
ef = ExempleFenetres()
ef.show()
app.exec()





