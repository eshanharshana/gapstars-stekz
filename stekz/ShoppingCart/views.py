from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from . models import Products, Order, OrderLine
from . serializer import ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """returns data for products"""
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    @action(detail=True, methods=['POST'])
    def add_to_cart(self, request, pk):
        """custom method to add items to cart. Cart is identified by the pk parameter"""
        if 'order_lines' in request.data:
            order = Order.objects.get(id=pk)
            order_lines = request.data.get('order_lines')
            # loops each line and create them and making sure they are linked to th order
            for line in order_lines:
                product_id = line.pop('product_id')
                product = Products.objects.get(id=product_id)
                OrderLine.objects.create(order_id=order, product_id=product, **line)
            serializer = OrderSerializer(order)
            # """returns response"""
            response = {
                'message': 'Item added to the card',
                'result': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide order lines'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def remove_from_cart(self, request, pk):
        """custom method to remove items to cart. Cart is identified by the pk parameter"""
        if 'item_ids' in request.data:
            order = Order.objects.get(id=pk)
            item_ids = request.data.get('item_ids')
            # delete items based on th ids
            for item in item_ids:
                OrderLine.objects.filter(id=item).delete()
            serializer = OrderSerializer(order)
            response = {
                'message': 'Item removed successfully',
                'result': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide item_ids'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def confirm_order(self, request, pk):
        """custom method to confirm order. Delivery date is also applied"""
        if 'delivery_date' in request.data:
            order = Order.objects.get(id=pk)
            order.delivery_date = request.data.get('delivery_date')
            order.status = 'confirmed'
            order.save()
            serializer = OrderSerializer(order)
            response = {
                'message': 'Order Confirmed Successfully !!',
                'result': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide the delivery_date'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)