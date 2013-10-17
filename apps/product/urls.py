from django.conf.urls.defaults import patterns, url
from apps.product.views import DisplayProducts

urlpatterns = patterns('',
    url(r'^display/$', DisplayProducts.as_view(), name='menu_create'),
    )