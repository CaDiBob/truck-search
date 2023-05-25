from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from location.models import Location


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

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return f'''
        Из {self.pickup_location.city}
        В {self.delivery_location.city}
        Вес: {self.weight}
        '''
