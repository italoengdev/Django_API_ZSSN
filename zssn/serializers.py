from rest_framework import serializers
from .models import Survivor, Item


class SurvivorSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = ('id', 'name', 'infected')


class ItemSerializer(serializers.ModelSerializer):
    survivor = SurvivorSerializer1(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'type', 'amount', 'value', 'survivor')


class SurvivorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Survivor
        fields = ('id', 'name', 'age', 'sex', 'latitude',
                  'longitude', 'infected', 'infection_count')

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get(
            'longitude', instance.longitude)
        instance.save()
        return instance
