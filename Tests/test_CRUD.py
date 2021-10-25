from Domain import rezervare
from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Postolachi Bogdan - Costel", "economy", 45.5, "da", lista)
    rezervare = lista[0]
    assert len(lista) == 1
    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "Postolachi Bogdan - Costel"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 45.5
    assert get_checkin(rezervare) == "da"


def test_sterge_rezervare():
    lista = adauga_rezervare("1", "Postolachi Bogdan - Costel", "economy", 45.5, "da", [])
    lista = adauga_rezervare("2", "Postolachi Roxana - Monica", "business", 60.0, "nu", lista)
    rezervare = lista[0]
    lista = sterge_rezervare("1", lista)
    assert len(lista) == 1
    assert get_by_id(get_id(rezervare), lista) is None


def test_modifica_rezervare():
    lista = adauga_rezervare("1", "Postolachi Bogdan - Costel", "economy", 45.5, "da", [])
    lista = adauga_rezervare("2", "Postolachi Roxana - Monica", "business", 60.0, "nu", lista)
    lista = modifica_rezervare("2", "Postolachi Roxana - Monica", "business", 65.0, "nu", lista)
    rezervare = lista[1]

    assert len(lista) == 2
    assert get_id(rezervare) == "2"
    assert get_nume(rezervare) == "Postolachi Roxana - Monica"
    assert get_clasa(rezervare) == "business"
    assert get_pret(rezervare) == 65.0
    assert get_checkin(rezervare) == "nu"


def test_get_by_id():
    lista = adauga_rezervare("1", "Postolachi Bogdan - Costel", "economy", 45.5, "da", [])
    lista = adauga_rezervare("2", "Postolachi Roxana - Monica", "business", 60.0, "nu", lista)
    assert get_id(get_by_id("1", lista)) ==  "1"
    assert get_nume(get_by_id("1", lista)) == "Postolachi Bogdan - Costel"
    assert get_clasa(get_by_id("1", lista)) == "economy"
    assert get_pret(get_by_id("1", lista)) == 45.5
    assert get_checkin(get_by_id("1", lista)) == "da"
