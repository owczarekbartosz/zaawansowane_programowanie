class Posesja:
    def __init__(self, miasto: str, ulica: str, nr_budynku: int, powierzchnia: float, cena: float):
        self._powierzchnia = powierzchnia
        self._miasto = miasto
        self._nr_budynku = nr_budynku
        self._ulica = ulica
        self._cena = cena

    @property
    def miasto(self):
        return self._miasto

    @property
    def ulica(self):
        return self._ulica

    @property
    def powierzchnia(self):
        return self._powierzchnia

    @property
    def cena(self):
        return self._cena

    @property
    def nr_budynku(self):
        return self._nr_budynku

    def __str__(self):
        return "Adres posesji: " + self._miasto + self._ulica + str(
            self._nr_budynku) + ". Powierzchnia w m2 wynosi " + str(self._powierzchnia) + " a cena jest równa " + str(
            self._cena)
