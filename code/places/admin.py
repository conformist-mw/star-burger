from django.contrib import admin

from .models import Place


@admin.action(description='Заполнить координаты мест')
def set_coordinates(modeladmin, request, queryset):
    for instance in queryset:
        instance.set_coordinates()


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    actions = [set_coordinates]
    list_display = ['id', 'lon', 'lat', 'address']
