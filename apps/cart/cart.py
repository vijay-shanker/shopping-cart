import uuid
from apps.cart.models import Cart
CART_ID = 'CART-ID'

class Cart(object):
    def __init__(self,request):
        self.request = request
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = Cart.objects.get(cart_id=cart_id)
            except Cart.DoesNotExists:
                cart = Cart.objects.create(cart_id=uuid.uuid4().hex)
        else:
            cart = Cart.objects.create(cart_id=uuid.uuid4().hex)

        request.session[CART_ID] = cart.id
        self.cart = cart

    def __iter__(self):
        for item in self.cart.cartitems.all():
            yield item
