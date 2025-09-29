from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QFrame
from PySide6.QtGui import QPixmap


class ComboEx(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.image_combobox = QComboBox()
        image_pyside = QPixmap("./images/pyside_train.png")
        self.image_combobox.addItem("Pyside train", image_pyside)
        image_batman = QPixmap("./images/batman.png")
        self.image_combobox.addItem("Batman et Robin", image_batman)
        self.image_combobox.setEditable(False)
        self.image_combobox.currentIndexChanged.connect(self.image_combobox_index_changed)

        disposition.addWidget(self.image_combobox)

        self.libelle_image = QLabel()
        self.libelle_image.setPixmap(self.image_combobox.currentData())
        disposition.addWidget(self.libelle_image)

        self.cours_combobox = QComboBox()
        self.cours_combobox.setEditable(True)
        self.cours_combobox.addItems(["420-SF3-RE", "Physique Ondes", "Prob et Stats"])
        self.cours_combobox.currentIndexChanged.connect(self.cours_combobox_index_changed)
        self.cours_combobox.currentTextChanged.connect(self.cours_combobox_text_changed)

        disposition_cours = QHBoxLayout()
        disposition_cours.addWidget(self.cours_combobox)

        cours_bouton_ajouter = QPushButton("+")
        cours_bouton_ajouter.clicked.connect(self.bouton_ajouter_clicked)

        cours_bouton_supprimer = QPushButton("-")
        cours_bouton_supprimer.clicked.connect(self.bouton_supprimer_clicked)

        disposition_cours.addWidget(cours_bouton_ajouter)
        disposition_cours.addWidget(cours_bouton_supprimer)
        disposition.addLayout(disposition_cours)

    def bouton_ajouter_clicked(self):
        self.cours_combobox.insertItem(0, "")
        self.cours_combobox.setCurrentIndex(0)

    def bouton_supprimer_clicked(self):
        self.cours_combobox.removeItem(self.cours_combobox.currentIndex())

    def cours_combobox_index_changed(self, index):
        pass

    def cours_combobox_text_changed(self, texte):
        self.cours_combobox.setItemText(self.cours_combobox.currentIndex(), texte)

    def image_combobox_index_changed(self, index):
        self.libelle_image.setPixmap(self.image_combobox.currentData())


app = QApplication()
ce = ComboEx()
ce.show()
app.exec()


