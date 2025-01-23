from django.shortcuts import render, redirect  # Import functions to render templates and redirect users
from django.contrib.auth import authenticate, login, logout  # Import Django authentication functions
from django.contrib import messages  # Import messages framework for user notifications
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
    # Check if the request method is POST (indicating form submission)
    if request.method == 'POST':
        # Safely get 'username' and 'password' from the submitted form using .get()
        # Using .get() prevents KeyError if the fields are missing in the request
        username = request.POST.get('username', '')  
        password = request.POST.get('password', '')

        # Check if both username and password were provided
        if username and password:
            # Authenticate the user using Django's built-in authentication system
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # If authentication is successful, log the user in
                login(request, user)
                
                # Add a success message to be displayed in the template
                messages.success(request, "You have successfully logged in!")
                
                # Redirect the user to the home page to prevent form resubmission
                return redirect('home')
            else:
                # If authentication fails, show an error message
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            # If username or password is missing, display an error message
            messages.error(request, "Both username and password are required.")

        # Redirect back to the home page after processing the form
        return redirect('home')

    # If the request method is GET (initial page load), render the login template
    return render(request, 'home.html', {'records':records})

def logout_user(request):
    """
    View function for logging out the user.
    - Logs the user out and redirects them to the home page.
    """
    
    # Log out the current user
    logout(request)
    
    # Add a success message for confirmation
    messages.success(request, "You have successfully logged out!")
    
    # Redirect the user to the home page after logging out
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()            
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')