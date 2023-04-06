from rest_framework import serializers
from .models import Survivor, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('type', 'amount')

class SurvivorSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Survivor
        fields = ('id', 'name', 'age', 'sex', 'latitude', 'longitude', 'infected', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        survivor = Survivor.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(survivor=survivor, **item_data)
        return survivor

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance
