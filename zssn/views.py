from http.client import METHOD_NOT_ALLOWED
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Survivor, Item
from .serializers import SurvivorSerializer, ItemSerializer


class SurvivorListCreateView(generics.ListCreateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    def create(self, request, *args, **kwargs):
        raise METHOD_NOT_ALLOWED("POST")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SurvivorRetrieveUpdateLocation(generics.RetrieveUpdateAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer


class SurvivorDetailAPIView(generics.RetrieveAPIView):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    def get(self, request, *args, **kwargs):
        survivor = self.get_object()
        queryset = Survivor.objects.exclude(id=survivor.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        survivor = self.get_object()
        queryset = Survivor.objects.exclude(id=survivor.id)
        serializer = self.get_serializer(
            queryset, many=True, data=request.data)
        serializer.is_valid(raise_exception=True)

        for other_survivor in queryset:
            infection_count = serializer.validated_data.get(
                str(other_survivor.id), None)
            if infection_count is not None:
                other_survivor.infection_count += infection_count
                if other_survivor.infection_count >= 3:
                    other_survivor.infected = True
                other_survivor.save()

        return Response(serializer.data)


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
