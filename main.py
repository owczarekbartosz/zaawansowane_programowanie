from models.developer import Developer
from models.dom import Dom
from models.mieszkanie import Mieszkanie
from models.zamówienie import Zamowienie

dom_1 = Dom("Warszawa", "Dębowa", 5, 90.4, 5000000, "posiada", 4)

mieszkanie_1 = Mieszkanie("Warszawa", 5, "Fiołkowa", 50.9, 500000, 7, 81)

mieszkanie_2 = Mieszkanie("Katowice", 5, "Fiołkowa", 50.9, 300000, 7, 81)

developer_1 = Developer(10, "Warszawa", "Zamieszkajmy!", "555 444 333")

zamowienie_1 = Zamowienie()

zamowienie_1.developer = developer_1
zamowienie_1.data_zamowienia = "15 czerwca 2022"
zamowienie_1.id_zamowienia = 1
zamowienie_1.dom = [dom_1]
zamowienie_1.mieszkanie = [mieszkanie_1, mieszkanie_2]
print(zamowienie_1)
print(zamowienie_1.wartosc_zamowienia())
print(zamowienie_1.suma_metrazu())
