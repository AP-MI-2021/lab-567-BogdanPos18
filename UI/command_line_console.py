from Logic.CRUD import adauga_rezervare, sterge_rezervare
from UI.console import show_all


def ui_cl_adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    try:
        pret1 = float(pret)
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Eroare: Nu ati introdus o clasa valida!")
            return lista
        lista = adauga_rezervare(id, nume, clasa, pret1, checkin, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_cl_sterge_rezervare(id, lista):
    try:
        lista = sterge_rezervare(id, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def command_line(lista):
    print("Pentru a introduce repetat linii de comanda, apasati 'y'. Cand doriti sa incheiati, apasati 'x'.")
    while True:
        optiune = input("Dati optiune: ")
        if optiune == 'y':
            string = input("Introduceti linia de comanda, cu operatiile separate prin ',' (operatii suportate: add, showall, delete): ")
            if string.count(',') == 0:
                show_all(lista)
            else:
                str1 = string.split(',')
                i = 0
                while i < len(str1):
                    if str1[i] == "add":
                        id = str1[i+1]
                        nume = str1[i+2]
                        clasa = str1[i+3]
                        pret = str1[i+4]
                        checkin = str1[i+5]
                        lista = ui_cl_adauga_rezervare(id, nume, clasa, pret, checkin, lista)
                        i += 6
                    elif str1[i] == "delete":
                        id = str1[i+1]
                        lista = ui_cl_sterge_rezervare(id, lista)
                        i += 2
                    elif str1[i] == "showall":
                        show_all(lista)
                        i += 1
        elif optiune == 'x':
            break
