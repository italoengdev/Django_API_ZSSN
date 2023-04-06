from django.contrib import admin
from .models import InventoryItem, Survivor, SurvivorInventory


class SurvivorInventoryInline(admin.TabularInline):
    model = SurvivorInventory
    extra = 1


class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'latitude', 'longitude', 'status')
    list_filter = ('status', 'gender')
    inlines = [SurvivorInventoryInline]


class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


admin.site.register(Survivor, SurvivorAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
