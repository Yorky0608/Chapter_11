from src import city_functions as cc


def test_city_country():
    city_country = cc.format_cc("Santiago", "Chile")
    assert city_country == "Santiago, Chile"