from PySide6.QtWidgets import QApplication, QFrame, QLineEdit, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QSize
import numpy as np


class SudokuApp(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku 2025")
        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.disposition_temps = QHBoxLayout()
        self.label_temps = QLabel("Temps:", alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.disposition_temps.addWidget(self.label_temps)
        self.affichage_temps = QLabel("0")
        self.disposition_temps.addWidget(self.affichage_temps)
        self.disposition_principale.addLayout(self.disposition_temps)

        self.disposition_jeu = QGridLayout()

        # Modèle
        self.jeu = SudokuJeu()

        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and i != 0 and j == 0:
                    ligne = QFrame()
                    ligne.setFrameShape(QFrame.Shape.HLine)
                    self.disposition_jeu.addWidget(ligne, i, 0, 1, 11)
                    continue

                if j % 3 == 0 and j != 0 and i == 0:
                    colonne = QFrame()
                    colonne.setFrameShape(QFrame.Shape.VLine)
                    self.disposition_jeu.addWidget(colonne, 0, j, 11, 1)
                    continue

                case_edit = QLineEdit("")
                case_edit.setMaxLength(1)
                case_edit.setInputMask("9")
                case_edit.setObjectName(f"case_{i}_{j}")
                case_edit.textEdited.connect(self.verifier_case)
                case_edit.setMaximumSize(QSize(SudokuJeu.GRANDEUR_CASE, SudokuJeu.GRANDEUR_CASE))
                self.disposition_jeu.addWidget(case_edit, i, j)

                if self.jeu.tableau_jeu[i][j] != 0:
                    case_edit.setText(str(self.jeu.tableau_jeu[i][j]))
                    case_edit.setEnabled(False)






        self.disposition_principale.addLayout(self.disposition_jeu)

        self.timer = QTimer(interval=1000)
        self.timer.timeout.connect(self.incrementer_temps)
        self.timer.start()

    def verifier_case(self):
        case = self.sender()
        nom_objet = case.objectName()
        ligne = nom_objet.split("_")[1]
        colonne = nom_objet.split("_")[2]

    def incrementer_temps(self):
        self.jeu.temps += 1
        self.affichage_temps.setNum(self.jeu.temps)




class SudokuJeu:

    GRANDEUR_CASE = 32

    def __init__(self):
        self.__tableau_jeu = np.zeros((9, 9), dtype=np.int8)
        self.__temps = 0

    @property
    def tableau_jeu(self):
        return self.__tableau_jeu

    @tableau_jeu.setter
    def tableau_jeu(self, tableau_jeu):
        self.__tableau_jeu = tableau_jeu

    @property
    def temps(self):
        return self.__temps

    @temps.setter
    def temps(self, temps: int):
        self.__temps = temps


    def verifier_gagnant(self):
        if 0 in self.tableau_jeu:
            return False

        return True


app = QApplication()
sa = SudokuApp()
sa.show()
app.exec()


