from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Grocery, Ingredient
from .serializers import GrocerySerializer, IngredientSerializer


class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.all()


class GroceryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        groceries = Grocery.objects.filter(family=user.id)
        serializer = GrocerySerializer(groceries, many=True)

        return Response(
            serializer.data,
        )

    def post(self, request, format=None):
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
