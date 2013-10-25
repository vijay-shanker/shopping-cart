shopping-cart
=============
This app is meant only for example purpose.

put cart in your installed apps, add this in urls:  url(r'^cart/', include('apps.cart.urls')) in your urls.py,
run syncdb or use south for schema.

This app assumes your product model has title and price fields.

Add to cart:
You can add "this" link to call AddToCart class for say a product_object instance by a with href as:

href="{% url 'add-to-cart' %}?app_label={{product_object|app_label}}&model_name={{product_object|class_name}}&obj_id={{sg.pk}}"   

The link to remove item from cart is obtained by rendering a form.

<form method="POST" action="{% url 'remove-from-cart' %}">{% csrf_token %}
    <input type="hidden" name="cartitem" value="{{cart_item.pk}}" />
    <input type="hidden" name="cart" value="{{cart.pk}}" />
    <input type="submit" value="remove">
</form>




