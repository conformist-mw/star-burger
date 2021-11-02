# Generated by Django 3.2.8 on 2021-11-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0044_added_restaurant_to_make_an_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processed', 'Обработан'), ('unprocessed', 'Необработан'), ('cancelled', 'Отменён')], default='unprocessed', max_length=15, verbose_name='Статус'),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together={('order', 'product')},
        ),
    ]
