from django.shortcuts import render, redirect
from .forms import RegistrationForm, Account 
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

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
            messages.success(request, 'Registration Successful.')
            return redirect('register')

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
            auth.login(request, user)  # Log in the user
            # messages.success(request, "You are now logged in.")  # Optional success message
            return redirect('home')  # Redirect to the home page
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


def activate(request):
    return