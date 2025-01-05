from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def handlelogin(request):
    return render(request, 'login.html')

def handlesignup(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        if password != confirmpassword:
            return HttpResponse("Oops! Password Incorrect.")

        
        try:
            if User.objects.get(username=uname):
                return HttpResponse("ALREADY USED")
        except:
            pass
        
        try:
            if User.objects.get(email=email):
                return HttpResponse("EMAIL USED ALREADY")
        except:
            pass
            
        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        return HTTPResponse("Signup Successfully!")
    
    return render(request, 'signup.html')