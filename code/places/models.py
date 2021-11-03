import requests

from django.db import models
from django.conf import settings


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

    def fetch_coordinates(self):
        base_url = 'https://geocode-maps.yandex.ru/1.x'
        return requests.get(base_url, params={
            'geocode': self.address,
            'apikey': settings.YANDEX_GEO_API_KEY,
            'format': 'json',
        })

    def set_coordinates(self):
        response = self.fetch_coordinates()
        if not response:
            return
        found_places = response.json()['response']['GeoObjectCollection']['featureMember']  # noqa: E501

        if not found_places:
            return

        most_relevant = found_places[0]

        self.lon, self.lat = most_relevant['GeoObject']['Point']['pos'].split(' ')  # noqa: E501
        self.save(update_fields=['lon', 'lat'])
