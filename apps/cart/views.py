# Create your views here.
import uuid
from django.views.generic import DetailView, TemplateView
from django.contrib.contenttypes.models import ContentType
from apps.cart.models import Cart, CartItem
from django.views.generic.edit import FormMixin
from django.views.generic.base import View, ContextMixin, TemplateResponseMixin
from django import forms
from django.shortcuts import get_object_or_404


class AddToCart(DetailView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'cart/add-to-cart.html'

    def get_object(self, queryset=None):
        return Cart.objects.get(cart_id=self.request.session['CART_ID'])

    def dispatch(self, request, *args, **kwargs):
        content_type = ContentType.objects.get(app_label=self.request.GET['app_label'], model=self.request.GET['model_name'].lower())
        model = content_type.model_class()
        product = model.objects.get(pk=self.request.GET['obj_id'])

        #check if cart exists for current session
        if 'CART_ID' in request.session.keys():
            cart = Cart.objects.get(cart_id=self.request.session._session_key)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, content_type=content_type, object_id=self.request.GET['obj_id'])
        else:
            cart_id = request.session._session_key
            cart = Cart.objects.create(cart_id=cart_id)
            cart_item = CartItem.objects.create(cart=cart, content_type=content_type, object_id=self.request.GET['obj_id'])
            request.session['CART_ID'] = cart_id

        return super(AddToCart, self).dispatch(request,*args,**kwargs) 

class RemoveFromCart(View, TemplateResponseMixin, ContextMixin):
    def get_template_names(self):
        return 'cart/add-to-cart.html'

    def post(self,request):
        cart = get_object_or_404(Cart, pk=self.request.POST.get('cart'))
        cartitem = get_object_or_404(CartItem, pk=self.request.POST.get('cartitem'))
        cartitem.delete()
        context = super(RemoveFromCart, self).get_context_data(**self.kwargs)
        context['cart'] = cart
        return self.render_to_response(context)















        
