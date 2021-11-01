from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.serializers import CharField, ModelSerializer

from .models import Order, OrderProduct


class OrderProductSerializer(ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


class OrderSerializer(ModelSerializer):

    firstname = CharField(source='first_name', max_length=50)
    lastname = CharField(source='last_name', max_length=50)
    phonenumber = PhoneNumberField(source='phone')
    products = OrderProductSerializer(many=True, allow_empty=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'firstname',
            'lastname',
            'address',
            'phonenumber',
            'products',
        ]

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product in products:
            OrderProduct.objects.create(
                order=order, price=product['product'].price, **product,
            )
        return order
