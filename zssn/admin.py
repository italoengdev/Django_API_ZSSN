from django.contrib import admin
from .models import Survivor, Item


class ItemInline(admin.TabularInline):
    model = Item


@admin.register(Survivor)
class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'latitude', 'longitude', 'infected')
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'survivor', 'value')
    list_filter = ('type',)
    search_fields = ('type', 'survivor__name')
