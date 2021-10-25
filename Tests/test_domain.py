from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin


def test_rezervare():
    rezervare = creeaza_rezervare("1", "Postolachi Bogdan - Costel", "economy", 45.5, "da")
    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "Postolachi Bogdan - Costel"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 45.5
    assert get_checkin(rezervare) == "da"
