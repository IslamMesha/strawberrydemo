import strawberry.django
from strawberry import auto

from strawberryapp import models


@strawberry.django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: "Color"


@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: list[Fruit]
