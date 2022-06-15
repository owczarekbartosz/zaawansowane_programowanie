from models.posesja import Posesja
from models.dom import Dom
from models.mieszkanie import Mieszkanie
from models.developer import Developer


class Zamowienie:

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, developer: Developer):
        self._developer = developer

    @property
    def id_zamowienia(self):
        return self._id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, id_zamowienia: int):
        self._id_zamowienia = id_zamowienia

    @property
    def data_zamowienia(self):
        return self._data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, data_zamowienia: str):
        self._data_zamowienia = data_zamowienia

    @property
    def dom(self):
        return self._dom

    @dom.setter
    def dom(self, dom: Dom):
        self._dom = dom

    @property
    def mieszkanie(self):
        return self._mieszkanie

    @mieszkanie.setter
    def mieszkanie(self, mieszkanie: Mieszkanie):
        self._mieszkanie = mieszkanie

    def __str__(self):
        return "Zamówienie złożone " + self._data_zamowienia

    def wartosc_zamowienia(self) -> float:
        return "łączna cena zamówienia: " + str(
            "{:.2f}".format(round((sum(m.cena for m in self._mieszkanie) + sum(d.cena for d in self._dom))),
                            2)) + " złotych"

    def suma_metrazu(self) -> float:
        return "łączny metraż zamówionych nieruchomości: " + str(
            sum(m.powierzchnia for m in self._mieszkanie) + sum(
                d.powierzchnia for d in self._dom)) + " metrów kwadratowych"
