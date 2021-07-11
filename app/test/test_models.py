import pytest
from ..models import Planet, People, Director, Producer, Film, SimpleNameModel


@pytest.mark.django_db
def test_simple_name_model():
    simple = SimpleNameModel("test")
    assert simple.name == 'test'


@pytest.mark.django_db
def test_planet_create():
    Planet.objects.create()
    assert Planet.objects.count() == 1


@pytest.mark.django_db
def test_people_create():
    director = Director.objects.create()
    film_dict = {
        'title': "Richard",
        'episode_id': 1,
        'opening_crawl': "90",
        'release_date': "1989-02-01",
        'director': director,
    }
    Film.objects.create(**film_dict)
    planet_dict = {
        'rotation_period': "1",
        'orbital_period': "1",
        'diameter': "1",
        'climate': "1",
        'gravity': "1",
        'terrain': "1",
        'surface_water': "1",
        'population': "1",
    }
    planet = Planet.objects.create(**planet_dict)
    people_dict = {
        'name': "Richard",
        'height': "170",
        'mass': "90",
        'hair_color': "BLACK",
        'skin_color': "BLACK",
        'eye_color': "BLACK",
        'gender': "MALE",
        'birth_year': "1989",
        'home_world': planet,
    }
    People.objects.create(**people_dict)
    assert People.objects.count() == 1


@pytest.mark.django_db
def test_director_create():
    Director.objects.create()
    assert Director.objects.count() == 1


@pytest.mark.django_db
def test_producer_create():
    Producer.objects.create()
    assert Producer.objects.count() == 1


@pytest.mark.django_db
def test_film_create():
    director = Director.objects.create()
    film_dict = {
        'title': "Richard",
        'episode_id': 1,
        'opening_crawl': "90",
        'release_date': "1989-02-01",
        'director': director,
    }
    film = Film.objects.create(**film_dict)
    assert Film.objects.count() == 1

