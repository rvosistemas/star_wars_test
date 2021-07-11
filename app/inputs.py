from graphene import ID
from graphene import String
from graphene import InputObjectType


class CreatePeopleInput(InputObjectType):
    id = ID(required=False)
    name = String(required=True)
    height = String(required=True)
    mass = String(required=True)
    hair_color = String(required=False)
    skin_color = String(required=False)
    eye_color = String(required=False)
    birth_year = String(required=False)
    gender = String(required=False)
    home_world_id = ID(required=True)
    film_id = ID(required=False)


class UpdatePeopleInput(InputObjectType):
    id = ID(required=True)
    name = String(required=False)
    height = String(required=False)
    mass = String(required=False)
    hair_color = String(required=False)
    skin_color = String(required=False)
    eye_color = String(required=False)
    birth_year = String(required=False)
    gender = String(required=False)
    home_world_id = ID(required=False)
