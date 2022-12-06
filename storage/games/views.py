from rest_framework import viewsets
from storage.games.models import Game
from storage.games.serializers import GameSerializer

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('release_date')
    serializer_class = GameSerializer