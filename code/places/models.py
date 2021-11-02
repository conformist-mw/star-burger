from django.db import models


class Place(models.Model):

    address = models.TextField('Адрес')
    lat = models.FloatField('Широта', default=0, blank=True)
    lon = models.FloatField('Долгота', default=0, blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'{self.address} {self.lat} {self.lon}'
