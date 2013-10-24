from django.contrib import admin
from apps.cart.models import Cart, CartItem, CartItemThrough
admin.site.register([Cart, CartItem, CartItemThrough])