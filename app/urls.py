from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", signin, name="signin"),
    path("cart/", cart, name="cart"),
    path("product/", allproduct, name="product"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
