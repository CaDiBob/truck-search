from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator
)

from location.models import Location


class Truck(models.Model):
    registration_plate = models.CharField(
        'Номер машины',
        validators=[
            RegexValidator(
                regex=r'^[1-9][0-9]{3}[A-Z]$',
                message='Неверный формат номера',
            )
        ],
        max_length=5,
        unique=True
    )
    load_capacity = models.IntegerField(
        'Грузоподъемность',
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        verbose_name='Локация',
        related_name='trucks'
    )

    class Meta:
        verbose_name = 'Грузовик'
        verbose_name_plural = 'Грузовики'

    def __str__(self):
        return str(self.registration_plate)
