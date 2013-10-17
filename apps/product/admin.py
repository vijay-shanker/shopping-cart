from django.contrib import admin
from apps.product.models import Eyeglass, Sunglass

admin.site.register([Eyeglass, Sunglass])