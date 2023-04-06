from rest_framework import generics, status
from rest_framework.response import Response
from .models import Survivor, Item
from .serializers import SurvivorSerializer, ItemSerializer


class SurvivorListCreateView(generics.ListCreateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SurvivorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


