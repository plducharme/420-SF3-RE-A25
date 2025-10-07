from PySide6.QtWidgets import QApplication, QRadioButton, QButtonGroup, QLabel, QFrame, QStackedLayout, QVBoxLayout, \
    QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class StackedLayoutAll(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple Stacked Layout Mode StackAll")
        self.disposition_verticale = QVBoxLayout()
        self.setLayout(self.disposition_verticale)

        self.groupe_bouton_selection = QButtonGroup(parent=self)
        self.groupe_bouton_selection.buttonClicked.connect(self.bouton_selection_clicked)

        self.label_gauche = QLabel("Label de gauche")
        self.label_droite = QLabel("Label de droite")
        self.label_droite.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.label_aussi_gauche = QLabel("Label aussi à gauche")
        self.label_centre_bas = QLabel("Label centre bas")
        self.label_centre_bas.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.label_pixmap = QLabel()
        self.image_beyond = QPixmap("./images/beyond.png")
        self.label_pixmap.setPixmap(self.image_beyond)

        # Création du stackedlayout
        self.disposition_empilee = QStackedLayout()
        # Utiliser le mode StackAll
        self.disposition_empilee.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.disposition_empilee.addWidget(self.label_gauche)
        self.bouton_selection_label_gauche = QRadioButton("Label gauche")
        self.groupe_bouton_selection.addButton(self.bouton_selection_label_gauche)
        self.bouton_selection_label_gauche.setChecked(True)
        self.disposition_empilee.setCurrentWidget(self.label_gauche)

        self.disposition_empilee.addWidget(self.label_droite)
        self.bouton_selection_label_droite = QRadioButton("Label droite")
        self.groupe_bouton_selection.addButton(self.bouton_selection_label_droite)

        self.disposition_empilee.addWidget(self.label_aussi_gauche)
        self.bouton_selection_label_aussi_gauche = QRadioButton("Label aussi gauche")
        self.groupe_bouton_selection.addButton(self.bouton_selection_label_aussi_gauche)

        self.disposition_empilee.addWidget(self.label_centre_bas)
        self.bouton_selection_label_centre_bas = QRadioButton("Label centre bas")
        self.groupe_bouton_selection.addButton(self.bouton_selection_label_centre_bas)

        self.disposition_empilee.addWidget(self.label_pixmap)
        self.bouton_selection_label_pixmap = QRadioButton("Label pixmap")
        self.groupe_bouton_selection.addButton(self.bouton_selection_label_pixmap)

        self.disposition_boutons = QGridLayout()
        self.disposition_boutons.addWidget(self.bouton_selection_label_gauche, 0, 0)
        self.disposition_boutons.addWidget(self.bouton_selection_label_aussi_gauche, 0, 1)
        self.disposition_boutons.addWidget(self.bouton_selection_label_droite, 0, 2)
        self.disposition_boutons.addWidget(self.bouton_selection_label_centre_bas, 1, 0)
        self.disposition_boutons.addWidget(self.bouton_selection_label_pixmap, 1, 1, 1, 2)

        self.disposition_verticale.addLayout(self.disposition_boutons)
        self.disposition_verticale.addLayout(self.disposition_empilee)

    def bouton_selection_clicked(self, bouton_clicked):

        match bouton_clicked:

            case self.bouton_selection_label_gauche:
                self.disposition_empilee.setCurrentWidget(self.label_gauche)

            case self.bouton_selection_label_aussi_gauche:
                self.disposition_empilee.setCurrentWidget(self.label_aussi_gauche)

            case self.bouton_selection_label_droite:
                self.disposition_empilee.setCurrentWidget(self.label_droite)

            case self.bouton_selection_label_centre_bas:
                self.disposition_empilee.setCurrentWidget(self.label_centre_bas)

            case self.bouton_selection_label_pixmap:
                self.disposition_empilee.setCurrentWidget(self.label_pixmap)


app = QApplication()
sla = StackedLayoutAll()
sla.show()
app.exec()
