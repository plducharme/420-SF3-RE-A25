from PySide6.QtWidgets import QApplication, QVBoxLayout, QFrame, QTextEdit, QProgressBar, QPushButton, QFileDialog, \
    QStatusBar
from PySide6.QtCore import QSize


class ProgressEx(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.texte_livre = QTextEdit()
        self.texte_livre.setMinimumSize(QSize(800, 600))
        disposition.addWidget(self.texte_livre)

        bouton_ouvrir = QPushButton("Ouvrir")
        bouton_ouvrir.clicked.connect(self.bouton_ouvrir_clicked)
        disposition.addWidget(bouton_ouvrir)

        self.barre_statut = QStatusBar()
        disposition.addWidget(self.barre_statut)

        self.barre_progression = QProgressBar()
        self.barre_statut.addPermanentWidget(self.barre_progression)
        self.barre_progression.hide()


    def bouton_ouvrir_clicked(self):
        chemin, filtre = QFileDialog.getOpenFileName(parent=self, caption="Choisir une fichier", filter="Fichier Texte (*.txt)")

        self.barre_progression.show()
        self.barre_progression.setMinimum(0)
        self.barre_progression.setValue(0)

        with open(file=chemin, mode="r", encoding="utf8") as fichier:
            lignes = fichier.readlines()
            self.barre_progression.setMaximum(len(lignes))

            for ligne in lignes:
                self.texte_livre.insertPlainText(ligne)
                self.barre_progression.setValue(self.barre_progression.value() + 1)

        self.barre_progression.hide()


app = QApplication()
pe = ProgressEx()
pe.show()
app.exec()


