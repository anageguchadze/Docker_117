from rest_framework import viewsets
from .models import Museum
from .serializers import MuseumSerializer

class MuseumViewSet(viewsets.ModelViewSet):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer