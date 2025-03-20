from django.shortcuts import render, redirect
from .forms import RegistrationForm, Account 
from django.contrib import messages

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
            messages.success(request, 'Registration Successful.')
            return redirect('register')

    context = {'form': form}  # Pass form instance to the template
    return render(request, 'accounts/register.html', context)  # Render the registration template

def login(request):
    return render(request, 'accounts/login.html') 

def logout(request):
    return render(request, 'accounts/logout.html') 
