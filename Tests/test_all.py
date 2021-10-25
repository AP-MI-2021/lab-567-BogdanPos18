from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare, test_get_by_id
from Tests.test_domain import test_rezervare
from Tests.test_functionalities import test_mutare_la_clasa_superioara


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_get_by_id()
    test_mutare_la_clasa_superioara()
