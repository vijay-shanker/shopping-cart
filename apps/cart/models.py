from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CartItem(Base):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type','object_id')
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(default=0.0, blank=True)
    
    def __str__(self):
        return self.content_object.title


class Cart(Base):
    cart_id = models.CharField(max_length=50, null=False)
    customer = models.ForeignKey(User,null=True,blank=True)
    customer_ip = models.IPAddressField(null=True, blank=True) 
    cartitems = models.ManyToManyField(CartItem,null=True,blank=True)
    num_cartitem = models.IntegerField(default=0)
    subtotal = models.FloatField(null=True,blank=True, default=0)

    def __str__(self):
        return self.cart_id