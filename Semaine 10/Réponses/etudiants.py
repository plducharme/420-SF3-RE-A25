import sqlite3

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QTableWidget, QTableWidgetItem, QGridLayout


class GestionnaireEtudiants(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionnaire d'étudiants")
        self.setGeometry(100, 100, 800, 600)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        disposition = QGridLayout()

        disposition.addWidget(QLabel("Nom:"), 0, 0)
        self.champ_nom = QLineEdit()
        disposition.addWidget(self.champ_nom, 0, 1)
        disposition.addWidget(QLabel("Prénom:"), 1, 0)
        self.champ_prenom = QLineEdit()
        disposition.addWidget(self.champ_prenom, 1, 1)
        disposition.addWidget(QLabel("Âge:"), 2, 0)
        self.champ_age = QLineEdit()
        disposition.addWidget(self.champ_age, 2, 1)
        disposition.addWidget(QLabel("No DA:"), 3, 0)
        self.champ_no_da = QLineEdit()
        disposition.addWidget(self.champ_no_da, 3, 1)

        disposition_boutons_suivant_precedent = QHBoxLayout()
        self.bouton_precedent = QPushButton("Précédent")
        self.bouton_precedent.setEnabled(False)
        self.bouton_precedent.clicked.connect(self.bouton_precedent_clicked)
        self.bouton_suivant = QPushButton("Suivant")
        self.bouton_suivant.setEnabled(False)
        self.bouton_suivant.clicked.connect(self.bouton_suivant_clicked)
        disposition_boutons_suivant_precedent.addWidget(self.bouton_precedent)
        disposition_boutons_suivant_precedent.addWidget(self.bouton_suivant)
        disposition.addLayout(disposition_boutons_suivant_precedent, 4,0, 1, 2)

        disposition_boutons = QHBoxLayout()
        self.bouton_ajouter = QPushButton("Nouveau")
        self.bouton_ajouter.clicked.connect(self.bouton_ajouter_clicked)
        self.bouton_enregistrer = QPushButton("Enregistrer")
        self.bouton_enregistrer.setEnabled(False)
        self.bouton_enregistrer.clicked.connect(self.bouton_enregistrer_clicked)
        self.bouton_supprimer = QPushButton("Supprimer")
        self.bouton_supprimer.setEnabled(False)
        self.bouton_supprimer.clicked.connect(self.bouton_supprimer_clicked)
        disposition_boutons.addWidget(self.bouton_ajouter)
        disposition_boutons.addWidget(self.bouton_enregistrer)
        disposition_boutons.addWidget(self.bouton_supprimer)
        disposition.addLayout(disposition_boutons, 5, 0, 1, 2)

        widget_central.setLayout(disposition)
        self.nouvel_enregistrement = False
        self.set_enabled_formulaire(False)

        self.client = ClientBD()
        self.index_enregistrement = 0
        self.liste_index = self.client.select_tous_no_da()
        if len(self.liste_index) > 0:
            self.afficher_etudiant()
            self.bouton_precedent.setEnabled(True)
            self.bouton_suivant.setEnabled(True)

    def bouton_ajouter_clicked(self):
        self.set_enabled_formulaire(True)
        self.bouton_enregistrer.setEnabled(True)
        self.bouton_supprimer.setEnabled(False)
        self.bouton_suivant.setEnabled(False)
        self.bouton_precedent.setEnabled(False)
        self.champ_nom.clear()
        self.champ_prenom.clear()
        self.champ_age.clear()
        self.champ_no_da.clear()
        self.nouvel_enregistrement = True


    def bouton_enregistrer_clicked(self):
        etudiant = Etudiant(int(self.champ_no_da.text()), self.champ_nom.text(), self.champ_prenom.text(), int(self.champ_age.text()))
        if self.nouvel_enregistrement:
            self.client.inserer(etudiant)
        else:
            self.client.mettre_a_jour(etudiant)
        self.bouton_precedent.setEnabled(True)
        self.bouton_suivant.setEnabled(True)
        self.bouton_supprimer.setEnabled(True)
        self.nouvel_enregistrement = False
        self.liste_index = self.client.select_tous_no_da()
        self.index_enregistrement = self.liste_index.index(etudiant.no_da)

    def bouton_supprimer_clicked(self):
        self.client.supprimer(int(self.champ_no_da.text()))
        self.liste_index.pop(self.index_enregistrement)
        self.set_enabled_formulaire(False)
        self.afficher_etudiant()

    def bouton_precedent_clicked(self):
        self.set_enabled_formulaire(True)
        if self.index_enregistrement == 0:
            return
        self.index_enregistrement -= 1
        self.afficher_etudiant()

    def bouton_suivant_clicked(self):
        self.set_enabled_formulaire(True)
        if self.index_enregistrement == len(self.liste_index) - 1:
            return
        self.index_enregistrement += 1
        self.afficher_etudiant()

    def set_enabled_formulaire(self, enabled: bool):
        self.champ_nom.setEnabled(enabled)
        self.champ_prenom.setEnabled(enabled)
        self.champ_age.setEnabled(enabled)
        self.champ_no_da.setEnabled(enabled)

    def afficher_etudiant(self):
        etudiant = self.client.get_etudiant(self.liste_index[self.index_enregistrement])
        self.champ_nom.setText(etudiant.nom)
        self.champ_prenom.setText(etudiant.prenom)
        self.champ_age.setText(str(etudiant.age))
        self.champ_no_da.setText(str(etudiant.no_da))

class Etudiant:
    def __init__(self, no_da: int, nom: str, prenom: str, age: int):
        self.no_da = no_da
        self.nom = nom
        self.prenom = prenom
        self.age = age


class ClientBD:

    def __init__(self):
        self.connexion = sqlite3.connect("etudiants.db")
        self.curseur = self.connexion.cursor()
        self.curseur.execute("CREATE TABLE IF NOT EXISTS etudiants (no_da INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER)")
        self.connexion.commit()


    def inserer(self, etudiant: Etudiant):
        self.curseur.execute("INSERT INTO etudiants VALUES (?, ?, ?, ?)", (etudiant.no_da, etudiant.nom, etudiant.prenom, etudiant.age))
        self.connexion.commit()

    def get_etudiant(self, no_da: int):
        self.curseur.execute("SELECT * FROM etudiants WHERE no_da = ?", (no_da,))
        resultat = self.curseur.fetchone()
        etudiant = Etudiant(resultat[0], resultat[1], resultat[2], resultat[3])
        return etudiant

    def supprimer(self, no_da: int):
        self.curseur.execute("DELETE FROM etudiants WHERE no_da = ?", (no_da,))
        self.connexion.commit()

    def mettre_a_jour(self, etudiant: Etudiant):
        self.curseur.execute("UPDATE etudiants SET nom = ?, prenom = ?, age = ? WHERE no_da = ?", (etudiant.nom, etudiant.prenom, etudiant.age, etudiant.no_da))
        self.connexion.commit()

    def select_tous_no_da(self):
        self.curseur.execute("SELECT no_da FROM etudiants")
        resultats = self.curseur.fetchall()
        etudiants = []
        for etudiant in resultats:
            etudiants.append(etudiant[0])
        return etudiants


app = QApplication()
fenetre = GestionnaireEtudiants()
fenetre.show()
app.exec()

