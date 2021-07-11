import pytest

from ..mutations import (
    CreatePlanetMutation,
    CreatePeopleMutation, UpdatePeopleMutation)


def test_create_planet():
    create_planet = CreatePlanetMutation.Input
    print("+"*100)
    print(create_planet)
    assert hasattr(create_planet, 'population')


def test_create_people():
    create_people = CreatePeopleMutation


def test_update_people():
    create_people = UpdatePeopleMutation
