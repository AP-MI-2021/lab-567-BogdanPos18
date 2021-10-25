from Domain.rezervare import creeaza_rezervare, get_id


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    '''
    Adauga o rezervare intr-o lista
    :param id: id-ul rezervarii
    :param nume: numele persoanei pe care se face rezervarea
    :param clasa: economy, economy plus sau business
    :param pret: pretul rezervarii
    :param checkin: da/nu
    :return: dictionar de tipul rezervare
    '''
    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def sterge_rezervare(id, lista):
    '''
    Sterge o rezervare dintr-o lista
    :param id:
    :param lista:
    :return:
    '''
    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
    '''
    Modifica o rezervare dintr-o lista dupa id
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''
    lista_noua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


def get_by_id(id, lista):
    '''
    Returneaza rezervarea cu id-ul dat ca parametru
    :param id:
    :param lista:
    :return:
    '''
    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None
