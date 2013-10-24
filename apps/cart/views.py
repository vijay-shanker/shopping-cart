# Create your views here.
import uuid
from django.views.generic import DetailView, TemplateView
from django.contrib.contenttypes.models import ContentType
from apps.cart.models import Cart, CartItem, CartItemThrough
from django.views.generic.edit import FormMixin
from django.views.generic.base import View
from django.views.generic.base import ContextMixin
from django.views.generic.base import TemplateResponseMixin
from django import forms
from django.shortcuts import get_object_or_404

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
        print request.session.keys()
        if 'CART_ID' in request.session.keys():
            cart = Cart.objects.get(cart_id = request.session['CART_ID'])
            cart_item, created = CartItem.objects.get_or_create(content_type=content_type, object_id=self.kwargs['obj_id'])
            cart_item_through, created_true = CartItemThrough.objects.get_or_create(cart=cart,cartitem=cart_item)
            if not created_true:
                cart_item_through.quantity +=1
                cart_item_through.save()
            cart.save()
        else:
            cart_id = uuid.uuid4().hex
            cart = Cart.objects.create(cart_id=cart_id)
            cart_item, created = CartItem.objects.get_or_create(content_type=content_type, object_id=self.kwargs['obj_id'])
            cart_item_through, created_true = CartItemThrough.objects.get_or_create(cart=cart,cartitem=cart_item)
            
            request.session['CART_ID'] = cart_id
        return super(AddToCart, self).dispatch(request,*args,**kwargs)


class RemoveFromCart(View, TemplateResponseMixin, ContextMixin):
    def get_template_names(self):
        return 'cart/add-to-cart.html'

    def post(self,request):
        cart = get_object_or_404(Cart, pk=self.request.POST.get('cart'))
        cartitem = get_object_or_404(CartItem, pk=self.request.POST.get('cartitem'))
        CartItemThrough.objects.get(cart=cart, cartitem=cartitem).delete()
        context = self.get_context_data(**self.kwargs)
        context['cart'] = cart
        return self.render_to_response(context)











        
