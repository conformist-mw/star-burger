from django.db import models

from places.models import Place


class Restaurant(models.Model):
    name = models.CharField(
        'название',
        max_length=50,
    )
    place = models.ForeignKey(
        to=Place,
        verbose_name='Адрес',
        related_name='restaurants',
        on_delete=models.CASCADE,
    )
    contact_phone = models.CharField(
        'контактный телефон',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'ресторан'
        verbose_name_plural = 'рестораны'

    def __str__(self):
        return self.name

    def get_products(self):
        return self.menu_items.values_list('product_id', flat=True)

    @staticmethod
    def get_products_map() -> dict['Restaurant', set]:
        return {
            restaurant: {
                item.product_id for item in restaurant.menu_items.all()
                if item.availability is True
            }
            for restaurant in (
                Restaurant.objects
                .select_related('place')
                .prefetch_related('menu_items')
            )
        }
