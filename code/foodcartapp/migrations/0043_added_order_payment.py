# Generated by Django 3.2.8 on 2021-11-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0042_added_order_timestamps'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('card', 'Картой'), ('cash', 'Наличными')], default='cash', max_length=10, verbose_name='Оплата'),
        ),
    ]
