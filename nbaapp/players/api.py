from rest_framework import viewsets, permissions
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [
        permissions.AllowAny
    ]