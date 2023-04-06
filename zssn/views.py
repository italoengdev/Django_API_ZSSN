from rest_framework import generics, status
from rest_framework.response import Response
from .models import Survivor, SurvivorInventory
from .serializers import SurvivorSerializer


class SurvivorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer


class SurvivorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer


