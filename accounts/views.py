from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


class Register(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Created",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response({"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
