from Domain.rezervare import get_nume, get_clasa, get_checkin, get_pret, get_id
from Logic.CRUD import modifica_rezervare


def mutare_la_clasa_superioara(nume, lista):
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            id = get_id(rezervare)
            pret = get_pret(rezervare)
            checkin = get_checkin(rezervare)
            if get_clasa(rezervare) == "economy":
                lista = modifica_rezervare(id, nume, "economy plus", pret, checkin, lista)
            elif get_clasa(rezervare) == "economy plus":
                lista = modifica_rezervare(id, nume, "business", pret, checkin, lista)
    return lista


def ieftinire_rezervari(percent, lista):
    percent_str = str(percent)
    if percent_str.isdigit() is False and percent < 0:
        raise ValueError("Nu ati introdus o valoare valida!")
    for rezervare in lista:
        if get_checkin(rezervare) == "da":
            id = get_id(rezervare)
            nume = get_nume(rezervare)
            clasa = get_clasa(rezervare)
            price = get_pret(rezervare)
            price -= percent / 100 * price
            checkin = get_checkin(rezervare)
            lista = modifica_rezervare(id, nume, clasa, price, checkin, lista)
    return lista


def det_pret_max_per_clasa(lista):
    max_e = 0
    max_ep = 0
    max_b = 0
    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare) > max_e:
                max_e = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare) > max_ep:
                max_ep = get_pret(rezervare)
        elif get_clasa(rezervare) == "business":
            if get_pret(rezervare) > max_b:
                max_b = get_pret(rezervare)
    return [max_e, max_ep, max_b]


def descrescator_dupa_pret(lista):
    return sorted(lista, reverse=True, key=get_pret)


def sume_preturi_per_nume(lista):
    nume = []
    for rezervare in lista:
        nume.append(get_nume(rezervare))
    no_duplicates = []
    for i in nume:
        if i not in no_duplicates:
            no_duplicates.append(i)
    sume = []
    for x in no_duplicates:
        s = 0
        for rezervare in lista:
            if x == get_nume(rezervare):
                s += get_pret(rezervare)
        sume.append([x, s])
    return sume


def get_undo_list(list, undo_list):
    undo_list.append(list)
    return undo_list
