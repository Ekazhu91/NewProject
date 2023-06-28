from django.urls import path

from .views import CartView, ProductView, ShopView, CartViewSet, WishlistView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'

urlpatterns = [
   path('cart/', CartView.as_view(), name='cart'),
   path('product/<int:id>/', ProductView.as_view(), name='product'),
   path('', ShopView.as_view(), name='shop'),
   path('', WishlistView.as_view(), name='wishlist')
]
