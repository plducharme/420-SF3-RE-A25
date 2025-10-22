from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QFileDialog, QPushButton, QLineEdit,
                               QWidget, QGridLayout, QFrame)
from PySide6.QtGui import QImage, QFont, QPalette, QColor
from PySide6.QtCore import QRect

# Image pris de https://docs.coronalabs.com/images/simulator/sprites-cat-running.png


class CoupeImage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.image_originale = None

        widget_central = QWidget()
        self.disposition = QGridLayout()
        widget_central.setLayout(self.disposition)
        self.setWindowTitle("Coupeur d'images")
        self.bouton_fichier = QPushButton("Sélectionner fichier")
        self.bouton_fichier.clicked.connect(self.afficher_dialogue_fichier)
        self.etiquette_fichier = QLabel("Fichier:")
        self.nom_fichier = QLineEdit("Fichier")
        self.nom_fichier.setPalette(QPalette(QColor(200, 200, 200)))
        police = self.nom_fichier.font()
        police.setItalic(True)
        self.nom_fichier.setFont(police)

        disposition_calculateur = QGridLayout()
        self.etiquette_largeur_fichier = QLabel("Largeur du fichier:")
        disposition_calculateur.addWidget(self.etiquette_largeur_fichier, 0, 0)
        self.largeur_image = QLabel("0")
        self.largeur_image.setEnabled(False)
        disposition_calculateur.addWidget(self.largeur_image, 0, 1)
        self.etiquette_hauteur_fichier = QLabel("Hauteur du fichier:")
        disposition_calculateur.addWidget(self.etiquette_hauteur_fichier, 1, 0)
        self.hauteur_image = QLabel("0")
        self.hauteur_image.setEnabled(False)
        disposition_calculateur.addWidget(self.hauteur_image, 1, 1)
        self.etiquette_nb_frames = QLabel("Nombre de frames par ligne:")
        self.nb_frames_par_ligne = QLineEdit("4")
        self.nb_frames_par_ligne.setInputMask("9")
        disposition_calculateur.addWidget(self.etiquette_nb_frames, 2, 0)
        disposition_calculateur.addWidget(self.nb_frames_par_ligne, 2, 1)
        self.etiquette_nb_lignes = QLabel("Nombre de lignes:")
        self.nb_lignes = QLineEdit("2")
        self.nb_lignes.setInputMask("9")
        disposition_calculateur.addWidget(self.etiquette_nb_lignes, 3, 0)
        disposition_calculateur.addWidget(self.nb_lignes, 3, 1)
        self.bouton_calcul = QPushButton("Calculer")
        self.bouton_calcul.clicked.connect(self.calculer)
        self.bouton_calcul.setEnabled(False)
        disposition_calculateur.addWidget(self.bouton_calcul, 4, 0, 1, 2)
        cadre_calculateur = QFrame()
        cadre_calculateur.setLayout(disposition_calculateur)
        cadre_calculateur.setFrameStyle(QFrame.Shape.WinPanel | QFrame.Shadow.Raised)

        self.etiquette_hauteur = QLabel("Hauteur Frame:")
        self.hauteur_coupe = QLineEdit("256")
        self.etiquette_largeur = QLabel("Largeur Frame:")
        self.largeur_coupe = QLineEdit("512")
        self.bouton_coupe = QPushButton("Coupez!")
        self.bouton_coupe.clicked.connect(self.couper_image)

        self.disposition.addWidget(self.etiquette_fichier, 0, 0)
        self.disposition.addWidget(self.nom_fichier, 0, 1)
        self.disposition.addWidget(self.bouton_fichier, 0, 2)
        self.disposition.addWidget(cadre_calculateur, 1, 0, 1, 3)
        self.disposition.addWidget(self.etiquette_hauteur, 2, 0)
        self.disposition.addWidget(self.hauteur_coupe, 2, 1, 1, 2)
        self.disposition.addWidget(self.etiquette_largeur, 3, 0)
        self.disposition.addWidget(self.largeur_coupe, 3, 1, 1, 2)
        self.disposition.addWidget(self.bouton_coupe, 4, 1, 1, 2)

        self.setCentralWidget(widget_central)

    def afficher_dialogue_fichier(self):
        fichier = QFileDialog.getOpenFileName(self, "Ouvrir Image", "./images", "Images (*.png *.jpg)")
        self.nom_fichier.setText(fichier[0])
        self.image_originale = QImage(fichier[0])
        self.largeur_image.setNum(self.image_originale.width())
        self.hauteur_image.setNum(self.image_originale.height())
        self.bouton_calcul.setEnabled(True)

    def couper_image(self):
        nom_fichier = self.nom_fichier.text()

        index = 0

        largeur_totale = int(self.largeur_image.text())
        hauteur_totale = int(self.hauteur_image.text())

        largeur_image = int(self.largeur_coupe.text())
        hauteur_image = int(self.hauteur_coupe.text())
        # Le QFileDialog retourne un tuple(nom_fichier, filtres)
        fichier_prefixe = nom_fichier.split(".")[0]
        fichier_extension = nom_fichier.split(".")[-1]

        for y in range(0, hauteur_totale, hauteur_image):
            for x in range(0, largeur_totale, largeur_image):
                # QImage.copy() permet de copy un QRect d'une image
                frame = self.image_originale.copy(QRect(x, y, largeur_image, hauteur_image))
                nouveau_fichier = fichier_prefixe+"_"+str(index)+"." + fichier_extension
                print(nouveau_fichier)
                frame.save(nouveau_fichier)
                index += 1

    def calculer(self):
        hauteur = round(int(self.hauteur_image.text()) / int(self.nb_lignes.text()))
        self.hauteur_coupe.setText(str(hauteur))
        largeur = round(int(self.largeur_image.text()) / int(self.nb_frames_par_ligne.text()))
        self.largeur_coupe.setText(str(largeur))


app = QApplication()
ci = CoupeImage()
ci.show()
app.exec()
