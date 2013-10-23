# Create your views here.
import uuid
from django.views.generic import DetailView, TemplateView
from django.contrib.contenttypes.models import ContentType
from apps.cart.models import Cart, CartItem
from django.views.generic.edit import FormMixin
from django.views.generic.base import View
from django import forms

class RemoveFromCartForm(forms.Form):
    cartitem = forms.HiddenInput()
    cart = forms.HiddenInput()


class AddToCart(DetailView):
    model = Cart 
    context_object_name = 'cart'
    template_name = 'cart/add-to-cart.html'

    def get_object(self,queryset=None):
        return Cart.objects.get(cart_id=self.request.session['CART_ID'])

    def dispatch(self, request, *args, **kwargs):
        content_type = ContentType.objects.get(app_label=self.kwargs['app_label'], model=self.kwargs['model_name'].lower())
        model = content_type.model_class()
        if 'CART_ID' in request.session.keys():
            cart = Cart.objects.get(cart_id = request.session['CART_ID'])
            cart_item, created = CartItem.objects.get_or_create(content_type=content_type, object_id=self.kwargs['obj_id'])
            cart.cartitems.add(cart_item)
            cart.save()
        else:
            cart_id = uuid.uuid4().hex
            cart = Cart.objects.create(cart_id=cart_id)
            cart_item, created = CartItem.objects.get_or_create(content_type=content_type, object_id=self.kwargs['obj_id'])
            cart.cartitems.add(cart_item)
            request.session['CART_ID'] = cart_id
        return super(AddToCart, self).dispatch(request,*args,**kwargs)

class RemoveFromCart(View):
    def post(self,request):
        print 'hahahaa try'











        
