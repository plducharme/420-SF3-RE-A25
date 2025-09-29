from PySide6.QtWidgets import QApplication, QFrame, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFontComboBox


class EditeurSimple(QFrame):

    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.setWindowTitle("Super Éditeur 3000")

        self.texte_edite = QTextEdit()
        self.texte_edite.setHtml("Je ne suis pas d'accord avec ce que vous <b>dites</b>, mais je défendrai jusqu'à la mort"
                                 " votre <i>droit</i> de le dire")
        disposition.addWidget(self.texte_edite)

        disposition_boutons = QHBoxLayout()
        self.bouton_gras = QPushButton("G")
        self.bouton_gras.clicked.connect(self.bouton_gras_clicked)
        self.bouton_italic = QPushButton("I")
        self.bouton_italic.clicked.connect(self.bouton_italic_clicked)
        self.bouton_gras_edit = QPushButton("G2")
        self.bouton_gras_edit.clicked.connect(self.bouton_gras_edit_clicked)

        disposition_boutons.addWidget(self.bouton_gras)
        disposition_boutons.addWidget(self.bouton_italic)
        disposition_boutons.addWidget(self.bouton_gras_edit)

        disposition.addLayout(disposition_boutons)

        self.selection_police = QFontComboBox()
        self.selection_police.currentFontChanged.connect(self.selection_police_changed)
        disposition.addWidget(self.selection_police)

    def bouton_gras_clicked(self):
        police = self.texte_edite.font()
        police.setBold(not police.bold())
        self.texte_edite.setFont(police)

    def bouton_italic_clicked(self):
        police = self.texte_edite.font()
        police.setItalic(not police.italic())
        self.texte_edite.setFont(police)

    def bouton_gras_edit_clicked(self):
        texte = self.texte_edite.textCursor().selectedText()
        texte = f"<b>{texte}</b>"
        self.texte_edite.textCursor().insertHtml(texte)

    def selection_police_changed(self, police):
        self.texte_edite.setFont(police)


app = QApplication()
es = EditeurSimple()
es.show()
app.exec()
