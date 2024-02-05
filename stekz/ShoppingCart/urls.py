from django.urls import path, include
from rest_framework import routers
from . import views
from . views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]