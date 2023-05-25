from django.db import models


class Location(models.Model):
    city = models.CharField('Город', max_length=100)
    state = models.CharField('Штат', max_length=100)
    zip_code = models.CharField('Индекс', max_length=10)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'{self.city} {self.lat} {self.lon}'
