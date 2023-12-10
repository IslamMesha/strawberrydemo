from django.db import models


class Fruit(models.Model):
    """A tasty treat"""

    name = models.CharField(
        max_length=20,
    )
    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        related_name="fruits",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="field description",
    )

    def __str__(self):
        return self.name
