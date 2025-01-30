from src import city_functions as cc


def test_city_country():
    city_country = cc.format_cc("Santiago", "Chile")
    assert city_country == "Santiago, Chile"

def test_city_country_population():
    city_country = cc.format_cc("Santiago", "Chile", 5000000)
    assert city_country == "Santiago, Chile - population 5000000"