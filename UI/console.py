from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import mutare_la_clasa_superioara, ieftinire_rezervari, det_pret_max_per_clasa, \
    descrescator_dupa_pret, sume_preturi_per_nume, get_undo_list


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara")
    print("5. Ieftinirea tuturor rezervarilor la care s-a facut checkin cu un procentaj citit")
    print("6. Determinarea pretului maxim pentru fiecare clasa")
    print("7. Ordonarea rezervarilor descrescator dupa pret")
    print("8. Afisarea sumelor preturilor pentru fiecare nume")
    print("u. Undo")
    print("a. Afiseaza tot")
    print("x. Iesire")


def ui_adauga_rezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy/economy plus/business): ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin: 'da/nu': ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Eroare: Nu ati introdus o clasa valida!")
            return lista
        if checkin != 'da' and checkin != 'nu':
            print("Eroare: Trebuie sa introduceti 'da'/'nu' ")
            return lista
        rezultat = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_rezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = sterge_rezervare(id, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_rezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy/economy plus/business): ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin: 'da/nu': ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Eroare: Nu ati introdus o clasa valida!")
            return lista
        if checkin != 'da' and checkin != 'nu':
            print("Eroare: Trebuie sa introduceti 'da'/'nu' ")
            return lista
        rezultat = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_mutare_la_clasa_superioara(lista):
    nume = input("Dati numele persoanei: ")
    rezultat = mutare_la_clasa_superioara(nume, lista)
    return rezultat


def ui_ieftinire_rezervari(lista):
    try:
        procentaj = input("Dati procentul cu care doriti sa se faca reducerea, in formatul 'x%': ")
        if procentaj.count('%') != 1:
            print("Eroare: Nu ati introdus corect procentajul!")
            return lista
        i = 0
        string = [procentaj[i:i+len(procentaj)-1] for i in range(0, len(procentaj), len(procentaj)-1)]
        percent = float(string[0])
        rezultat = ieftinire_rezervari(percent, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_det_pret_max_per_clasa(lista):
    preturi = det_pret_max_per_clasa(lista)
    print("Preturile maxime pentru clasele economy/economy plus/business sunt: ", preturi)


def ui_descrescator_dupa_pret(lista):
    rezultat = descrescator_dupa_pret(lista)
    return rezultat


def ui_afisare_sume_preturi_per_nume(lista):
    lista_sume = sume_preturi_per_nume(lista)
    for x in lista_sume:
        y = "nume: {}, suma: {}".format(x[0], x[1])
        print(y)


def ui_undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        return undo_list.pop()
    return lista


def ui_redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        return redo_list.pop()
    return lista


def show_all(lista):
    if lista == []:
        print("[]")
    for rezervare in lista:
        print(to_string(rezervare))


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Alegeti operatia: ")
        if optiune == '1':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_adauga_rezervare(lista)
        elif optiune == '2':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_sterge_rezervare(lista)
        elif optiune == '3':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_modifica_rezervare(lista)
        elif optiune == '4':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_mutare_la_clasa_superioara(lista)
        elif optiune == '5':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_ieftinire_rezervari(lista)
        elif optiune == '6':
            ui_det_pret_max_per_clasa(lista)
        elif optiune == '7':
            undo_list = get_undo_list(lista, undo_list)
            redo_list.clear()
            lista = ui_descrescator_dupa_pret(lista)
        elif optiune == '8':
            ui_afisare_sume_preturi_per_nume(lista)
        elif optiune == 'u':
            if len(undo_list) > 0:
               lista = ui_undo(lista, undo_list, redo_list)
            else:
                print("Nu se mai poate face undo!")
        elif optiune == 'r':
            if len(redo_list) > 0:
                lista = ui_redo(lista, undo_list, redo_list)
            else:
                print("Nu se mai poate face redo!")
        elif optiune == 'a':
            show_all(lista)
        elif optiune == 'x':
            break
