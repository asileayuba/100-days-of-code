from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserProfileForm, UserForm
from .models import Account, UserProfile
from orders.models import Order, OrderProduct
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from carts.views import _cart_id
from carts.models import Cart, CartItem
import requests

# Create your views here.

def register(request):
    """
    Handles user registration.
    Displays the registration form and processes form submission.
    """
    form = RegistrationForm()  # Initialize an empty registration form

    if request.method == 'POST':  # Check if the form is submitted
        form = RegistrationForm(request.POST)  # Populate the form with submitted data
        if form.is_valid():  # Validate the form
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Generate a username from the email (before the @ symbol)
            username = email.split("@")[0]
            
            # Create a new user with the extracted data
            user = Account.objects.create_user(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                username=username, 
                password=password
            )
            user.phone_number = phone_number  # Assign phone number to the user
            user.save()  # Save the user instance
            
            # USER ACTIVATION 
            current_site = get_current_site(request)
            mail_subject = "Welcome to Ayubuy! Activate Your Account to Start Shopping"
            message = render_to_string('accounts/account_verification_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, "Thank you for registering! A verification email has been sent to your inbox. Please check your email and confirm your account.")
            return redirect('/accounts/login/?command=verification&email='+email)

    context = {'form': form}  # Pass form instance to the template
    return render(request, 'accounts/register.html', context)  # Render the registration template


def login(request):
    """
    Handles user login functionality.
    """
    if request.method == 'POST':  # Check if the request method is POST
        email = request.POST['email']  # Get the email from form data
        password = request.POST['password']  # Get the password from form data

        # Authenticate user using email and password
        user = auth.authenticate(email=email, password=password)

        if user is not None:  # If authentication is successful
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    
                    # Getting the product variation by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                        
                    # Get the cart item from the user to access his product variation
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    
                    # product_variation = [1, 2, 3, 4, 5, 6]
                    # ex_var_list = [4, 6, 3, 5]
                    
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
                                
            except: 
                pass
            auth.login(request, user) 
            messages.success(request, "You are now logged in.") 
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout/
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')  # Display error message
            return redirect('login')  # Redirect back to login page if authentication fails

    return render(request, 'accounts/login.html')  # Render the login page for GET requests


@login_required(login_url='login')  # Restrict access to logged-in users; redirect to login if not authenticated
def logout(request):
    """
    Handles user logout functionality.
    """
    auth.logout(request)  # Log out the user
    messages.success(request, 'You are logged out.')  # Display success message
    return redirect('login')  # Redirect to login page after logout


def activate(request, uidb64, token):
    """
    Handles account activation when a user clicks the activation link in their email.
    """
    try:
        # Decode the base64-encoded user ID
        uid = urlsafe_base64_decode(uidb64).decode()
        # Retrieve the user object based on the decoded ID
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None  # Set user to None if any error occurs

    # Validate the user and check if the token is correct
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True  # Activate the user's account
        user.save()  # Save the changes to the database
        messages.success(request, 'Congratulations! Your account has been activated.')  # Success message
        return redirect("login")  # Redirect the user to the login page
    else:
        messages.error(request, 'Invalid activation link')  # Error message if activation fails
        return redirect('register')  # Redirect to the registration page if the link is invalid
    
@login_required(login_url= 'login')
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    order_count =orders.count()
    context = {
        "order_count": order_count,
    }
    return render(request, 'accounts/dashboard.html', context)
    
    
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            # Reset password email
            current_site = get_current_site(request)
            mail_subject = "Reset Your Password"
            message = render_to_string('accounts/reset_password_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        
        
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has expired!')
        return redirect('login')
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password == '' or confirm_password == '':
            messages.error(request, 'Both password fields are required!')
            return redirect('resetPassword')

        if password == confirm_password:
            uid = request.session.get('uid')
            if not uid:
                messages.error(request, 'Session expired or invalid request. Try again.')
                return redirect('resetPassword')

            try:
                user = Account.objects.get(pk=uid)
                user.set_password(password)
                user.save()
                del request.session['uid']  # Clear session after reset
                messages.success(request, 'Password reset successfully!')
                return redirect('login')
            except Account.DoesNotExist:
                messages.error(request, 'User not found. Try again.')
                return redirect('resetPassword')

        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('resetPassword')

    return render(request, 'accounts/resetPassword.html')


@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)


@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        user = Account.objects.get(username__exact=request.user.username)
        
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, "Password updated successfully.")
                return redirect('change_password')
            else:
                messages.error(request, 'Please enter valid current password.')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'accounts/change_password.html')



@login_required(login_url='login')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity
    context = {
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, 'accounts/order_detail.html', context)