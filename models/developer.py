class Developer:
    def __init__(self, staz: int, miasto: str, nazwa_firmy: str, telefon: str):
        self._staz = staz
        self._miasto = miasto
        self._nazwa_firmy = nazwa_firmy
        self._telefon = telefon

    @property
    def staz(self):
        return self._staz

    @property
    def miasto(self):
        return self._miasto

    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy

    @property
    def telefon(self):
        return self._telefon

    def __str__(self):
        return "Deweloper " + self._nazwa_firmy + " znajdujący się w " + self._miasto + " posiada " + str(
            self._staz) + " lata stażu w branży. Numer kontaktowy " + str(self._telefon)
