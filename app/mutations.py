import graphene
from graphql_relay import from_global_id
from graphene import Mutation
from django.db import connection

from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process
from .inputs import CreatePeopleInput, UpdatePeopleInput


class CreatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)
    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreatePlanetMutation(planet=planet)


class CreatePeopleMutation(Mutation):

    people = graphene.Field(PeopleType)

    class Arguments:
        input = CreatePeopleInput(required=True)

    @staticmethod
    def mutate(root, info, input):
        film_id = input.pop("film_id")
        people = People.objects.create(**input)
        if film_id:
            cursor = connection.cursor()
            sql = f'INSERT INTO film_characters (film_id, people_id) values({film_id},{people.pk})'
            cursor.execute(sql)
            cursor.close()
        return CreatePeopleMutation(people=people)


class UpdatePeopleMutation(Mutation):

    people = graphene.Field(PeopleType)

    class Arguments:
        input = UpdatePeopleInput(required=True)

    @staticmethod
    def mutate(root, info, input):
        People.objects.filter(pk=input.get('id')).update(**input)
        people = People.objects.get(pk=input.get('id'))
        return UpdatePeopleMutation(people=people)
