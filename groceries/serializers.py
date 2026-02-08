from rest_framework.serializers import ModelSerializer

from .models import Grocery, Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "category"]


class GrocerySerializer(ModelSerializer):
    class Meta:
        model = Grocery
        fields = ["id", "ingredents", "family"]
