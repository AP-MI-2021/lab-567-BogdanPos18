from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import mutare_la_clasa_superioara, ieftinire_rezervari


def test_mutare_la_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Postolachi Bogdan", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "Postolachi Bogdan", "economy plus", 45.0, "nu", lista)
    lista = adauga_rezervare("3", "Postolachi Bogdan", "business", 60.0, "da", lista)
    lista = adauga_rezervare("4", "Cristian", "business", 60.0, "nu", lista)
    assert get_clasa(get_by_id("1", mutare_la_clasa_superioara("Postolachi Bogdan", lista))) == "economy plus"
    assert get_clasa(get_by_id("1", mutare_la_clasa_superioara("Postolachi Bogdan", lista))) == "business"
    assert get_clasa(get_by_id("3", mutare_la_clasa_superioara("Postolachi Bogdan", lista))) == "business"
    assert get_clasa(get_by_id("4", mutare_la_clasa_superioara("Cristian", lista))) == "business"


def test_ieftinire_rezervari():
    lista = []
    lista = adauga_rezervare("1", "Postolachi Bogdan", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "Postolachi Bogdan", "economy plus", 45.0, "nu", lista)
    lista = adauga_rezervare("3", "Postolachi Bogdan", "business", 60.0, "da", lista)
    lista = adauga_rezervare("4", "Cristian", "business", 60.0, "nu", lista)
    lista_noua = ieftinire_rezervari(20, lista)
    assert get_pret(get_by_id("1", lista_noua)) == 32.0
    assert get_pret(get_by_id("2", lista_noua)) == 45.0
    assert get_pret(get_by_id("3", lista_noua)) == 48.0
    assert get_pret(get_by_id("4", lista_noua)) == 60.0
