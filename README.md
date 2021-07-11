# star_wars_test

Star wars tribute project where you can manage franchise information such as movies, characters, directors among others

## Requirements

-   [Python](https://www.python.org/) (realizado en python 3.8)
-   [Django](https://github.com/django/django)
-   [Django Filter](https://github.com/carltongibson/django-filter)
-   [Django model utils](https://github.com/jazzband/django-model-utils)
-   [Graphene](https://github.com/graphql-python/graphene-django)
-   [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project

```
git clone https://github.com/rvosistemas/star_wars_test.git
```

Create a virtual enviroment

```
python -m venv nombre_entorno_virtual
```

Move into de repo and install dependencies

```
pip install -r requirements.txt
```

Run migrations and load fixtures

```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server

```
python manage.py runserver
```

If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Test endpoints in graphql

createPlanet

```
mutation {
createPlanetMutation(input: {
name: "tierra",
rotationPeriod:"2",
orbitalPeriod: "2",
diameter:"2",
climate:"2",
gravity:"2",
terrain: "2",
surfaceWater:"1"
population: "100",
})
{
planet {
name
rotationPeriod
orbitalPeriod
diameter
climate
gravity
 terrain
surfaceWater
population
}
}
}
```

createPeople

```
mutation {
createPeopleMutation(input: {
name: "Richard",
height:"170",
mass: "90",
hairColor:"BLACK",
skinColor:"BLACK",
eyeColor:"BLACK",
gender: "MALE",
birthYear:"1989"
homeWorldId: 1,
filmId:1
})
{
people {
name
height
hairColor
skinColor
eyeColor
mass
 gender
birthYear
id
}
}
}
```

updatePeople

```
mutation {
updatePeopleMutation(input: {
id: 94,
name: "Richard vivas",
height:"170",
mass: "90",
hairColor:"BLACK",
skinColor:"BLACK",
eyeColor:"BLACK",
gender: "MALE",
birthYear:"1989"
homeWorldId: 1
})
{
people {
id
name
height
hairColor
skinColor
eyeColor
mass
 gender
birthYear
id
}
}
}
```

### Runing the tests with Pytest

Run test with pytest in console

```
export DJANGO_SETTINGS_MODULE=swapi.settings
pytest --cov-report term --cov=app app/test/
```
