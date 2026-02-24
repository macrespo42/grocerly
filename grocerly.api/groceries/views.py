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
        if user.family is None:
            return Response({"detail": "User does not belong to a family."}, status=status.HTTP_400_BAD_REQUEST)
        groceries = Grocery.objects.filter(family=user.family)
        serializer = GrocerySerializer(groceries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        if user.family is None:
            return Response({"detail": "User does not belong to a family."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(family=user.family)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
