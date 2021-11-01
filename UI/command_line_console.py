from Logic.CRUD import adauga_rezervare, sterge_rezervare
from UI.console import show_all


def ui_adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
    return lista


def ui_sterge_rezervare(id, lista):
    lista = sterge_rezervare(id, lista)
    return lista


def command_line(lista):
    string = input("Introduceti linia de comanda, cu elementele separate prin ';' (operatii suportate: add, showall, delete): ")
    if string.count(';') == 0:
        str = string
    else:
        str = string.split(';')
    for i in range(len(str)):
        if str[i].count(',') == 0:
            str1 = str[i]
        else:
            str1 = str[i].split(',')
        j = 0
        if str1[j] == "add":
            id = str1[j+1]
            nume = str1[j+2]
            clasa = str1[j+3]
            pret = float(str1[j+4])
            checkin = str1[j+5]
            lista = ui_adauga_rezervare(id, nume, clasa, pret, checkin, lista)
            print(lista)
        elif str1[j] == "delete":
            id = str1[j+1]
            lista = ui_sterge_rezervare(id, lista)
        elif str1[j] == "showall":
            show_all(lista)

