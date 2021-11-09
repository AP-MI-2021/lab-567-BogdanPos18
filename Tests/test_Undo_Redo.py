from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import get_undo_list
from UI.console import ui_undo, ui_redo


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []
    undo_list = get_undo_list(lista, undo_list)
    lista = adauga_rezervare("1", "a", "economy", 50, "da", lista)
    undo_list = get_undo_list(lista, undo_list)
    lista = adauga_rezervare("2", "b", "economy plus", 100, "da", lista)
    undo_list = get_undo_list(lista, undo_list)
    lista = adauga_rezervare("3", "c", "business", 150, "da", lista)
    assert len(lista) == 3
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is not None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    undo_list = get_undo_list(lista, undo_list)
    redo_list.clear()
    lista = adauga_rezervare("1", "a", "economy", 50, "da", lista)
    undo_list = get_undo_list(lista, undo_list)
    redo_list.clear()
    lista = adauga_rezervare("2", "b", "economy plus", 100, "da", lista)
    undo_list = get_undo_list(lista, undo_list)
    redo_list.clear()
    lista = adauga_rezervare("3", "c", "business", 150, "da", lista)
    assert len(lista) == 3
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is not None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is not None
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is not None
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    undo_list = get_undo_list(lista, undo_list)
    redo_list.clear()
    lista = adauga_rezervare("4", "d", "business", 150, "nu", lista)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is not None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is not None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is None
    lista = ui_redo(lista, undo_list, redo_list)
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is not None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    assert get_by_id("4", lista) is not None
