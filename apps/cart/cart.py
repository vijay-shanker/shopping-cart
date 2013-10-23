import uuid
from apps.cart.models import Cart
CART_ID = 'CART_ID'

class Cart(object):
    def __init__(self,request):
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

    def add_to_cart(self, app_label, model_name, obj_id, quantity=1 ):
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        cart_item = CartItem.objects.create(content_type=content_type,object_id=obj_id, quantity=quantity)
        self.cart.cartitems.add(cart_item)


