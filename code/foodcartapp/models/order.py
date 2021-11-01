from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .product import Product


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'products__product',
        )


class OrderProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('product')


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    address = models.TextField('Адрес')
    phone = PhoneNumberField('Номер Телефона')

    objects = OrderManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone}'


class OrderProduct(models.Model):
    order = models.ForeignKey(
        verbose_name='Заказ',
        to=Order,
        related_name='products',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        verbose_name='Продукт',
        to=Product,
        related_name='ordered_products',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
    quantity = models.PositiveSmallIntegerField('Количество', default=0)

    objects = OrderProductManager()

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return self.product.name
