def creeaza_rezervare(id, nume, clasa, pret, checkin):
    '''
    Creeaza o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: string
    :param checkin: string
    :return: o tupla ce contine o rezervare
    '''
    return [id, nume, clasa, pret, checkin]


def get_id(rezervare):
    '''
    Ia id-ul rezervarii
    :param rezervare: tupla de tipul rezervare
    :return: id-ul rezervarii
    '''
    return rezervare[0]


def get_nume(rezervare):
    '''
    Ia numele persoanei pe care este facuta rezervarea
    :param rezervare: tupla de tipul rezervare
    :return: numele persoanei pe care este facuta rezervarea
    '''
    return rezervare[1]


def get_clasa(rezervare):
    '''
    Ia clasa rezervarii
    :param rezervare: tupla de tipul rezervare
    :return: clasa
    '''
    return rezervare[2]


def get_pret(rezervare):
    '''
    Ia pretul rezervarii
    :param rezervare: tupla de tipul rezervare
    :return: pretul
    '''
    return rezervare[3]


def get_checkin(rezervare):
    '''
    Ia checkin-ul rezervarii
    :param rezervare: tupla de tipul rezervare
    :return: checkin
    '''
    return rezervare[4]


def to_string(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare),
    )
