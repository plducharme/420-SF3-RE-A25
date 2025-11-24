from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QVBoxLayout, QTextEdit, QMenu
import pandas as pd


class RuellesVertes(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Données sur les ruelles vertes de Montréal")

        self.widget_central = QFrame()
        self.setCentralWidget(self.widget_central)
        self.disposition_principale = QVBoxLayout()
        self.widget_central.setLayout(self.disposition_principale)

        self.action_importer_csv = QAction("Importer un csv")
        self.action_importer_csv.triggered.connect(self.importer_csv)

        self.action_quitter = QAction("Quitter")
        self.action_quitter.setShortcut("Ctrl+Q")
        self.action_quitter.triggered.connect(self.close)

        self.action_exporter_excel = QAction("Exporter vers excel")
        self.action_exporter_excel.triggered.connect(self.exporter_excel)


        self.barre_menu = self.menuBar()
        self.menu_fichier = QMenu("&Fichier")
        self.menu_import_export = QMenu("Import/Export")

        self.barre_menu.addMenu(self.menu_fichier)
        self.menu_fichier.addMenu(self.menu_import_export)
        self.menu_import_export.addAction(self.action_importer_csv)
        self.menu_fichier.addSeparator()
        self.menu_fichier.addAction(self.action_quitter)



    def importer_csv(self):
        pass

    def exporter_excel(self):
        pass


app = QApplication()
rv = RuellesVertes()
rv.show()
app.exec()
