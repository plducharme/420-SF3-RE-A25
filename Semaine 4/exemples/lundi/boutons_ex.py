from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QCheckBox, QRadioButton, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox


class BoutonEx(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.marque_dodge_checkbox = QCheckBox("Dodge")
        self.marque_kia_checkbox = QCheckBox("Kia")
        self.marque_tesla_checkbox = QCheckBox("Tesla")
        self.marque_tesla_checkbox.setIcon(QIcon("lightning.png"))
        self.marque_tesla_checkbox.setChecked(True)

        disposition_marques = QHBoxLayout()
        disposition_marques.addWidget(self.marque_dodge_checkbox)
        disposition_marques.addWidget(self.marque_kia_checkbox)
        disposition_marques.addWidget(self.marque_tesla_checkbox)
        disposition.addLayout(disposition_marques)

        self.couleur_rouge = QRadioButton("Rouge")
        self.couleur_bleu = QRadioButton("Bleu")
        self.couleur_mauve = QRadioButton("Mauve")

        self.groupe_couleurs = QButtonGroup()
        self.groupe_couleurs.addButton(self.couleur_rouge)
        self.groupe_couleurs.addButton(self.couleur_bleu)
        self.groupe_couleurs.addButton(self.couleur_mauve)

        disposition_couleur = QHBoxLayout()
        disposition_couleur.addWidget(self.couleur_rouge)
        disposition_couleur.addWidget(self.couleur_bleu)
        disposition_couleur.addWidget(self.couleur_mauve)

        disposition.addLayout(disposition_couleur)

        groupe_motopropulseur = QGroupBox()
        groupe_motopropulseur.setCheckable(True)
        groupe_motopropulseur.setTitle("Groupe Motopropulseur")

        disposition_groupe_motopropulseur = QVBoxLayout()
        disposition_groupe_motopropulseur.addWidget(QRadioButton("V4"))
        disposition_groupe_motopropulseur.addWidget(QRadioButton("V6"))
        disposition_groupe_motopropulseur.addWidget(QRadioButton("V8"))
        disposition_groupe_motopropulseur.addWidget(QRadioButton("Électrique"))

        groupe_motopropulseur.setLayout(disposition_groupe_motopropulseur)
        disposition.addWidget(groupe_motopropulseur)


app = QApplication()
be = BoutonEx()
be.show()
app.exec()





app = QApplication()
be = BoutonEx()
be.show()
app.exec()




