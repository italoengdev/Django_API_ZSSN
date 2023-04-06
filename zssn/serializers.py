from rest_framework import serializers
from .models import Survivor, InventoryItem, SurvivorInventory


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'value']


class SurvivorSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Survivor
        fields = ['id', 'name', 'age', 'gender', 'latitude',
                  'longitude', 'status', 'inventory_items']

    def create(self, validated_data):
        inventory_items_data = validated_data.pop('inventory_items')
        survivor = Survivor.objects.create(**validated_data)
        for item_data in inventory_items_data:
            item = InventoryItem.objects.get(
                id=item_data['inventory_item']['id'])
            SurvivorInventory.objects.create(
                survivor=survivor, inventory_item=item, quantity=item_data['quantity'])
        return survivor

    def update(self, instance, validated_data):
        inventory_items_data = validated_data.pop('inventory_items')
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get(
            'longitude', instance.longitude)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        items_to_delete = instance.inventory_items.all()
        for item in items_to_delete:
            item.delete()

        for item_data in inventory_items_data:
            item = InventoryItem.objects.get(
                id=item_data['inventory_item']['id'])
            SurvivorInventory.objects.create(
                survivor=instance, inventory_item=item, quantity=item_data['quantity'])

        return instance
