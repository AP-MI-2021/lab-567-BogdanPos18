from Domain.rezervare import to_string, creeaza_rezervare
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import mutare_la_clasa_superioara, ieftinire_rezervari


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara")
    print("5. Ieftinirea tuturor rezervarilor la care s-a facut checkin cu un procentaj citit")
    print("6. Determinarea pretului maxim pentru fiecare clasa")
    print("7. Ordonarea rezervarilor descrescator dupa pret")
    print("8. Afisarea sumelor preturilor pentru fiecare nume")
    print("9. Undo")
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
        lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_rezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        lista = sterge_rezervare(id, lista)
        return lista
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
        lista = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_mutare_la_clasa_superioara(lista):
    nume = input("Dati numele persoanei: ")
    lista = mutare_la_clasa_superioara(nume, lista)
    return lista


def ui_ieftinire_rezervari(lista):
    try:
        procentaj = input("Dati procentul cu care doriti sa se faca reducerea, in formatul 'x%': ")
        i = 0
        string = [procentaj[i:i+len(procentaj)-1] for i in range(0, len(procentaj), len(procentaj)-1)]
        percent = float(string[0])
        lista = ieftinire_rezervari(percent, lista)
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    if lista == []:
        print("[]")
    for rezervare in lista:
        print(rezervare)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Alegeti operatia: ")
        if optiune == '1':
            lista = ui_adauga_rezervare(lista)
        elif optiune == '2':
            lista = ui_sterge_rezervare(lista)
        elif optiune == "3":
            lista = ui_modifica_rezervare(lista)
        elif optiune == '4':
            lista = ui_mutare_la_clasa_superioara(lista)
        elif optiune == "5":
            lista = ui_ieftinire_rezervari(lista)
        elif optiune == 'a':
            show_all(lista)
        elif optiune == 'x':
            break
