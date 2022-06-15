from models.posesja import Posesja


class Dom(Posesja):
    def __init__(self, miasto: str, ulica: str, nr_budynku: int, powierzchnia: float, cena: float, garaz: str,
                 kondygnacje: int):
        super().__init__(miasto, ulica, nr_budynku, powierzchnia, cena)
        self._garaz = garaz
        self._kondygnacje = kondygnacje

    @property
    def garaz(self):
        return self._garaz

    @property
    def kondygnacje(self):
        return self._kondygnacje

    def __str__(self):
        return super().__str__() + " Dom ma " + str(self._kondygnacje) + " kondygnacje oraz " + self._garaz + ' garaż'
