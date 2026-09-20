from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    pass
