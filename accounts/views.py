from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Hello world. You are at the account index")


class ProtectedHello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello from authenticated grocerly"}
        return Response(content)
