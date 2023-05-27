from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

from location.models import Location
from truck.models import Truck
from cargo.sevices import get_distance_from_truck_to_load


class CargoQuerySet(models.QuerySet):

    def get_trucks_with_distance(self):
        trucks = Truck.objects.select_related('location')
        for cargo in self:
            trucks_with_distance = [
                {
                    'registration_plate': truck.registration_plate,
                    'distance': get_distance_from_truck_to_load(truck, cargo)
                }
                for truck in trucks
            ]
            cargo.trucks_with_distance = trucks_with_distance
        return self

    def get_nearest_trucks(self):
        for cargo in self:
            distances = cargo.trucks_with_distance
            nearest_trucks = len(
                [
                    distance['distance']
                    for distance in distances
                    if distance['distance'] <= 450
                ]
            )
            cargo.nearest_trucks = nearest_trucks
        return self


class Cargo(models.Model):
    pickup_location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        verbose_name='Место получения груза',
        related_name='pickup_locations'
    )
    delivery_location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        verbose_name='Место доставки груза',
        related_name='delivery_locations'
    )
    weight = models.IntegerField(
        'Вес',
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    description = models.TextField(
        'Описание груза'
    )
    objects = CargoQuerySet.as_manager()

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return f'''
        Из {self.pickup_location.city}
        В {self.delivery_location.city}
        Вес: {self.weight}
        '''
