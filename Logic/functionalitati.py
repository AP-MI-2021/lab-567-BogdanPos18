from Domain.rezervare import get_nume, get_clasa


def mutare_la_clasa_superioara(nume, lista):
    lista_noua = []
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == "economy":
                rezervare[2] = "economy plus"
            elif get_clasa(rezervare) == "economy plus":
                rezervare[2] = "business"
        lista_noua.append(rezervare)
    return lista_noua
