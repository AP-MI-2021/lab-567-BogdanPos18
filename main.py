from Tests.test_all import run_all_tests
from UI.command_line_console import command_line
from UI.console import run_menu


def main():
    lista = []
    run_all_tests()
    print("Pentru primul meniu, apasati 1, pentru cel de al doilea, apasati 2")
    p = input("Alegeti meniul: ")
    if p == '1':
        command_line(lista)
    elif p == '2':
        run_menu(lista)


main()
