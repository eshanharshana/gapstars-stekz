from django.contrib import admin
from . models import Products
from . models import Order
from . models import OrderLine

# registering admin sites
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderLine)
