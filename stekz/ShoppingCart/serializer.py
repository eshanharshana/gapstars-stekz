from rest_framework import serializers
from . models import Products
from . models import Order
from . models import OrderLine


class ProductSerializer(serializers.ModelSerializer):
    """serializer for products"""
    class Meta:
        model = Products
        fields = ['id', 'name', 'price']


class OrderLineSerializer(serializers.ModelSerializer):
    """serializer for Order Lines"""
    class Meta:
        model = OrderLine
        fields = ['id', 'name', 'product_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """serializer for orders"""
    order_lines = OrderLineSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date_time', 'order_lines', 'status', 'delivery_date']

    def create(self, validated_data):
        """Inheriting create function and create nested items for order lines"""
        order_lines = validated_data.pop('order_lines')
        order = Order.objects.create(**validated_data)
        for line in order_lines:
            OrderLine.objects.create(order_id=order, **line)
        return order
