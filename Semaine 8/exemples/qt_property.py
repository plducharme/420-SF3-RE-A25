from PySide6.QtCore import QObject, Property


class ObjetQt(QObject):

    def __init__(self):
        super().__init__()
        self._ma_valeur = 1

    # Getter
    @Property(int)
    def ma_valeur(self):
        return self._ma_valeur

    @ma_valeur.setter
    def ma_valeur(self, nouvelle_valeur: int):
        self._ma_valeur = nouvelle_valeur


obj = ObjetQt()
obj.ma_valeur = 9
print(obj.ma_valeur)
