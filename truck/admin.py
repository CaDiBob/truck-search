from django.contrib import admin

from truck.models import Truck
from location.models import Location
from cargo.models import Cargo


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    raw_id_fields = ['location', ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    raw_id_fields = ['pickup_location', 'delivery_location']
