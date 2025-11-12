from city_functions import make_city


def test_city_country():
    assert make_city("Santiago", "Chile") == "Santiago, Chile"


def test_city_country_population():
    assert (
        make_city("Santiago", "Chile", population=1000000)
        == "Santiago, Chile - population 1000000"
    )
