from models.posesja import Posesja


class Mieszkanie(Posesja):
    def __init__(self, miasto: str, nr_budynku: int, ulica: str, powierzchnia: float, cena: float, pietro: int,
                 nr_mieszkania: int):
        super().__init__(miasto, ulica, nr_budynku, powierzchnia, cena)
        self._pietro = pietro
        self._nr_mieszkania = nr_mieszkania

    @property
    def pietro(self):
        return self._pietro

    @property
    def nr_mieszkania(self):
        return self._nr_mieszkania

    def __str__(self):
        return super().__str__() + " Mieszkanie znajduje sie na " \
                                   "" + str(self._pietro) + " pietrze. Nr mieszkania: " + str(self._nr_mieszkania)
