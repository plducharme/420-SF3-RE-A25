from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton


class LineEdit(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple QLineEdit")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        libelle_nom_serie = QLabel("Nom:")
        self.nom_valeur = QLineEdit()
        self.nom_valeur.setMaxLength(128)

        disposition_nom = QHBoxLayout()
        disposition_nom.addWidget(libelle_nom_serie)
        disposition_nom.addWidget(self.nom_valeur)

        disposition.addLayout(disposition_nom)

        libelle_serie_annee = QLabel("Année:")
        self.annee_valeur = QLineEdit()
        self.annee_valeur.setInputMask("9999")

        disposition_annee = QHBoxLayout()
        disposition_annee.addWidget(libelle_serie_annee)
        disposition_annee.addWidget(self.annee_valeur)

        disposition.addLayout(disposition_annee)

        self.bouton_sauvegarder = QPushButton("Sauvegarder")
        self.bouton_sauvegarder.clicked.connect(self.bouton_sauvegarder_clicked)
        disposition.addWidget(self.bouton_sauvegarder)

    def bouton_sauvegarder_clicked(self):
        print(f"{self.nom_valeur.text()}-{self.annee_valeur.text()}")
        self.nom_valeur.clear()
        self.annee_valeur.clear()


app = QApplication()
le = LineEdit()
le.show()
app.exec()


