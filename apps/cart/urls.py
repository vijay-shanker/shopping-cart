from django.conf.urls.defaults import patterns, url
from apps.cart.views import *

urlpatterns = patterns('',
    url(r'^add_to_cart/$', AddToCart.as_view(), name='add-to-cart'),
    url(r'^remove-from-cart/$', RemoveFromCart.as_view(), name="remove-from-cart"),
    )
