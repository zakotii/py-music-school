from rest_framework.viewsets import ModelViewSet
from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
