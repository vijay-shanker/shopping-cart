from django.conf.urls.defaults import patterns, url
from apps.cart.views import  AddToCart

urlpatterns = patterns('',
    url(r'^add_to_cart/(?P<app_label>\w+)/(?P<model_name>\w+)/(?P<obj_id>\d+)/$', AddToCart.as_view(), name='add-to-cart'),
    )
