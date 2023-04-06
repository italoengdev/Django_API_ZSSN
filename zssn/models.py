from django.db import models


class Survivor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=(
        ('M', 'Male'), ('F', 'Female')))
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    infected = models.BooleanField(default=False)


class Item(models.Model):
    WATER = 'Water'
    FOOD = 'Food'
    MEDICATION = 'Medication'
    AMMUNITION = 'Ammunition'
    ITEM_TYPES = (
        (WATER, 'Water'),
        (FOOD, 'Food'),
        (MEDICATION, 'Medication'),
        (AMMUNITION, 'Ammunition'),
    )
    ITEM_VALUES = {
        WATER: 4,
        FOOD: 3,
        MEDICATION: 2,
        AMMUNITION: 1,
    }
    type = models.CharField(max_length=255, choices=ITEM_TYPES)
    amount = models.PositiveIntegerField()

    @property
    def value(self):
        return self.ITEM_VALUES[self.type]

    survivor = models.ForeignKey(
        Survivor, on_delete=models.CASCADE, related_name='items')

    class Meta:
        unique_together = ('type', 'survivor')
