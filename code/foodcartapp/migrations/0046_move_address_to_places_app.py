# Generated by Django 3.2.9 on 2021-11-03 21:08

from django.db import migrations, models
import django.db.models.deletion


def set_places_with_coordinates(apps, schema_editor):
    Order = apps.get_model('foodcartapp', 'Order')
    Place = apps.get_model('places', 'Place')
    Restaurant = apps.get_model('foodcartapp', 'Restaurant')

    for restaurant in Restaurant.objects.all():
        place = Place.objects.create(address=restaurant.address)
        restaurant.place = place
        restaurant.save()

    for order in Order.objects.all():
        place = Place.objects.create(address=order.address)
        order.place = place
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('foodcartapp', '0045_unique_order_product_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='places.place', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='places.place', verbose_name='Адрес'),
        ),
        migrations.RunPython(set_places_with_coordinates, migrations.RunPython.noop)
    ]