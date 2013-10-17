# Create your views here.
from django.views.generic import ListView
from apps.product.models import Sunglass, Eyeglass

class DisplayProducts(ListView):
    model = Sunglass
    context_object_name = 'sunglass_objects'
    template_name = "product/display_products.html"

    def get_context_data(self,**kwargs):
        context = super(DisplayProducts, self).get_context_data(**kwargs)
        context['eyeglasses'] = Eyeglass.objects.all()
        return context

