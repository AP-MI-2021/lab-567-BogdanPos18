from Domain.rezervare import to_string, creeaza_rezervare
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import mutare_la_clasa_superioara


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
    print("x. Iesire")


def ui_adauga_rezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa (economy/economy plus/business): ")
    pret = float(input("Dati pretul: "))
    checkin = input("Dati checkin: 'da/nu': ")
    lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
    return lista


def ui_sterge_rezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    lista = sterge_rezervare(id, lista)
    return lista


def ui_modifica_rezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa (economy/economy plus/business): ")
    pret = float(input("Dati pretul: "))
    checkin = input("Dati checkin: 'da/nu': ")
    rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
    lista = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
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
            show_all(lista)
        elif optiune == '2':
            lista = ui_sterge_rezervare(lista)
            show_all(lista)
        elif optiune == "3":
            lista = ui_modifica_rezervare(lista)
            show_all(lista)
        elif optiune == '4':
            nume = input("Dati numele persoanei: ")
            lista = mutare_la_clasa_superioara(nume, lista)
            show_all(lista)
        elif optiune == 'x':
            break
