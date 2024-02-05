from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.CharField(max_length=100)
    order_date_time = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField(null=True)
    status = models.CharField(choices=[('draft', 'Draft'), ('confirmed', 'Confirmed')], default='draft', max_length=10)


class OrderLine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.RESTRICT, related_name='product')
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='order_lines')


