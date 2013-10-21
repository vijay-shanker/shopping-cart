# Create your views here.
from django.views.generic import DetailView

class AddToCart(DetailView):
    template_name = 'cart/add-to-cart.html'