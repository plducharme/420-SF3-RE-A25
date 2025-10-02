from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QGridLayout, QPushButton, QLabel, QVBoxLayout, \
    QMessageBox
from PySide6.QtGui import QPixmap
import random


class Demineur(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Démineur 2025")

        # Modèle
        self.largeur_jeu = 16
        self.hauteur_jeu = 16
        self.nombre_mines = 32
        self.jeu = DemineurJeu(self.largeur_jeu, self.hauteur_jeu, self.nombre_mines)

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.disposition_score = QHBoxLayout()
        self.libelle_score = QLabel("Score:")
        self.libelle_total_score = QLabel("0")
        self.disposition_score.addWidget(self.libelle_score)
        self.disposition_score.addWidget(self.libelle_total_score)
        self.disposition_principale.addLayout(self.disposition_score)

        self.disposition_jeu = QGridLayout()

        for i in range(self.jeu.hauteur):
            for j in range(self.jeu.largeur):
                case_demineur = QPushButton()
                case_demineur.setObjectName(f"case_{i}_{j}")
                case_demineur.clicked.connect(self.case_clicked)
                case_demineur.setMinimumSize(DemineurJeu.GRANDEUR_CASE, DemineurJeu.GRANDEUR_CASE)
                case_demineur.setMaximumSize(DemineurJeu.GRANDEUR_CASE, DemineurJeu.GRANDEUR_CASE)
                self.disposition_jeu.addWidget(case_demineur, i, j)

        self.disposition_principale.addLayout(self.disposition_jeu)


    def case_clicked(self):
        case_cliquee = self.sender()
        nom_case = case_cliquee.objectName()
        case_split = nom_case.split("_")
        ligne = int(case_split[1])
        colonne = int(case_split[2])

        if self.jeu.tableau_jeu[ligne][colonne] == 0:
            self.jeu.tableau_jeu[ligne][colonne] = 2
            case_cliquee.setEnabled(False)
            if self.jeu.verifier_gagnant():
                QMessageBox.information(self, "Bravo!", "Vous avez gagné")
                self.jeu = DemineurJeu(self.largeur_jeu, self.hauteur_jeu, self.nombre_mines)
        elif self.jeu.tableau_jeu[ligne][colonne] == 1:
            QMessageBox.critical(self, "Partie Perdu", "Vous avez sauté!\nMeilleure chance la prochaine fois!")
            self.jeu = DemineurJeu(self.largeur_jeu, self.hauteur_jeu, self.nombre_mines)







class DemineurJeu:

    GRANDEUR_CASE = 32

    def __init__(self, largeur: int=16, hauteur: int=16, nombre_mines: int=32):
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__nombre_mines = nombre_mines
        self.__tableau_jeu = []
        self.__mines_trouvees = 0

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur

    @property
    def hauteur(self):
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, hauteur):
        self.__hauteur = hauteur

    @property
    def nombre_mines(self):
        return self.__nombre_mines

    @nombre_mines.setter
    def nombre_mines(self, nombre_mines):
        self.nombre_mines = nombre_mines

    @property
    def tableau_jeu(self):
        return self.__tableau_jeu

    @tableau_jeu.setter
    def tableau_jeu(self, tableau_jeu):
        self.__tableau_jeu = tableau_jeu

    @property
    def mines_trouvees(self):
        return self.__mines_trouvees

    @mines_trouvees.setter
    def mines_trouvees(self, mine_trouvees):
        self.__mines_trouvees = mine_trouvees

    def creer_jeu(self):
        jeu = []
        for i in range(self.hauteur):
            ligne = []
            for j in range(self.largeur):
                ligne.append(0)
            jeu.append(ligne)

        mine_a_placer = self.nombre_mines

        while mine_a_placer > 0:
            ligne = random.randint(0, self.hauteur - 1)
            colonne = random.randint(0, self.largeur - 1)

            if jeu[ligne][colonne] == 0:
                jeu[ligne][colonne] = 1
                mine_a_placer -= 1
            else:
                continue
        self.__tableau_jeu = jeu


    def verifier_gagnant(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if self.tableau_jeu[i][j] == 0:
                    return False
        return True




app = QApplication()
demineur = Demineur()
demineur.show()
app.exec()

