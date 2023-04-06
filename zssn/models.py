from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Survivor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Masculino'),
        (FEMALE, 'Feminino'),
    ]
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    STATUS_CHOICES = [
        ('NI', 'Não infectado'),
        ('I', 'Infectado'),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default='NI')
    inventory_items = models.ManyToManyField(
        InventoryItem, through='SurvivorInventory', related_name='survivors')

    def __str__(self):
        return self.name


class SurvivorInventory(models.Model):
    survivor = models.ForeignKey(Survivor, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.survivor.name} - {self.inventory_item.name}'
