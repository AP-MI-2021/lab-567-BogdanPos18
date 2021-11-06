from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import mutare_la_clasa_superioara, ieftinire_rezervari, det_pret_max_per_clasa, \
    descrescator_dupa_pret, sume_preturi_per_nume


def test_mutare_la_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Postolachi Bogdan", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "Postolachi Bogdan", "economy plus", 45.0, "nu", lista)
    lista = adauga_rezervare("3", "Postolachi Bogdan", "business", 60.0, "da", lista)
    lista = adauga_rezervare("4", "Cristian", "business", 60.0, "nu", lista)
    assert get_clasa(get_by_id("1", mutare_la_clasa_superioara("Postolachi Bogdan", lista))) == "economy plus"
    assert get_clasa(get_by_id("2", mutare_la_clasa_superioara("Postolachi Bogdan", lista))) == "business"
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


def test_det_pret_max_per_clasa():
    lista = []
    lista = adauga_rezervare("1", "a", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "b", "economy", 45.0, "da", lista)
    lista = adauga_rezervare("3", "c", "economy", 20.2, "da", lista)
    lista = adauga_rezervare("4", "d", "economy plus", 60.0, "da", lista)
    lista = adauga_rezervare("5", "e", "economy plus", 70.0, "da", lista)
    lista = adauga_rezervare("6", "f", "business", 80.0, "da", lista)
    lista = adauga_rezervare("7", "g", "business", 90.0, "nu", lista)
    assert (det_pret_max_per_clasa(lista) == [45.0, 70.0, 90.0]) is True


def test_descrescator_dupa_pret():
    lista = []
    lista = adauga_rezervare("1", "a", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "b", "economy", 45.0, "da", lista)
    lista = adauga_rezervare("3", "c", "economy", 20.2, "da", lista)
    lista = adauga_rezervare("4", "d", "economy plus", 60.0, "da", lista)
    lista = adauga_rezervare("5", "e", "economy plus", 70.0, "da", lista)
    lista = adauga_rezervare("6", "f", "business", 80.0, "da", lista)
    lista = adauga_rezervare("7", "g", "business", 90.0, "nu", lista)
    sorted_list = descrescator_dupa_pret(lista)
    assert get_pret(sorted_list[0]) == 90.0
    assert get_pret(sorted_list[1]) == 80.0
    assert get_pret(sorted_list[2]) == 70.0
    assert get_pret(sorted_list[3]) == 60.0
    assert get_pret(sorted_list[4]) == 45.0
    assert get_pret(sorted_list[5]) == 40.0
    assert get_pret(sorted_list[6]) == 20.2


def test_sume_preturi_per_nume():
    lista = []
    lista = adauga_rezervare("1", "a", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "b", "economy", 45.0, "da", lista)
    lista = adauga_rezervare("3", "b", "economy", 20.2, "da", lista)
    lista = adauga_rezervare("4", "a", "economy plus", 60.0, "da", lista)
    lista = adauga_rezervare("5", "c", "economy plus", 70.0, "da", lista)
    lista = adauga_rezervare("6", "d", "business", 80.0, "da", lista)
    lista = adauga_rezervare("7", "c", "business", 90.0, "nu", lista)
    lista_sume = sume_preturi_per_nume(lista)
    assert len(lista_sume) == 4
    assert lista_sume[0] == ["a", 100.0]
    assert lista_sume[1] == ["b", 65.2]
    assert lista_sume[2] == ["c", 160.0]
    assert lista_sume[3] == ["d", 80.0]
