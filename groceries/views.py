from rest_framework.viewsets import ModelViewSet

from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.all()
