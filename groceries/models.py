from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.contrib.gis.db.models import CharField
from django.db import models
from accounts.models import Family


class Ingredients(models.Model):
    name: CharField = models.CharField(max_length=42)
    category: CharField = models.CharField(max_length=42)
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class GroceriesList(models.Model):
    ingredients: ForeignKey[Ingredients] = models.ForeignKey(
        to=Ingredients, on_delete=models.CASCADE
    )
    family: ForeignKey[Family] = models.ForeignKey(to=Family, on_delete=models.CASCADE)
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Ingredients: {self.ingredients.name} in family: {self.family.name}"
