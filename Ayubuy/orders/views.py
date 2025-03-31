from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import json
from store.models import Product
from django.db.models import F
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body["orderID"])
    # print("Received Payment Data:", body)
    
    # Store transaction details inside payment model
    new_payment = Payment(
        user = request.user,
        payment_id = body["transID"],
        payment_method = body["payment_method"],
        amount_paid = order.order_total,
        status = body["status"],
    )
    new_payment.save()
    
    order.payment = new_payment
    order.is_ordered = True
    order.save()
    
    # Move the cart items to Order Product table
    cart_items = CartItem.objects.filter(user=request.user)  # Renamed to 'cart_items'
    
    for item in cart_items:
        orderproduct = OrderProduct(
            order=order,
            payment=new_payment,
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            product_price=item.product.price,  # Corrected reference
            ordered=True
        )
        orderproduct.save()
        
        cart_item = CartItem.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id=orderproduct.id)
        orderproduct.variation.set(product_variation)
        orderproduct.save()
    
    # Reduce the quantity of the sold products
    for item in cart_items:
        Product.objects.filter(id=item.product.id).update(stock=F('stock') - item.quantity)
    
    # Clear the cart
    CartItem.objects.filter(user=request.user).delete()
    
    # Send order received email to customer
    mail_subject = "🎉 Order Confirmation - We've Received Your Order!"
    message = render_to_string('orders/order_received_email.html', {
        'user': request.user,
        'order': order,
    })

    to_email = order.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
            
    # Send order number and transaction id back to sendData method via JsonResponse
    
    return render(request, 'orders/payments.html')


def place_order(request, total=0, quantity=0):
    current_user = request.user

    # Check if the cart is empty
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100  
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Create and store order
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime('%Y%m%d')  # Order of date

            # Ensure data.id exists before using it
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            
            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }

            return render(request, 'orders/payments.html', context)

    return redirect('checkout')


def order_complete(request):
    return render(request, 'orders/order_complete.html')