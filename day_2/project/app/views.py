from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact

# This imports below is for sending emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        query = Contact(name=fname, email=femail, phoneNumber=phone, description=desc)
        query.save()
        # Emails sending starts from here
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_meassage = mail.EmailMessage(
            f"Email is from {fname}",
            f"UserEmail: {femail} \nUserPhoneNumber: {phone}\n\n\n Query: {desc}",
            from_email,
            ["asileayuba@gmail.com"],
            connection=connection,
        )
        connection.send_messages([])

        messages.info(
            request, "Thank you for reaching out to us! We'll respond to you shortly."
        )
        return redirect("/contact")
    return render(request, "contact.html")


def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successfully!")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/login")

    return render(request, "login.html")


def handlesignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        if password != confirmpassword:
            messages.warning(request, "Password does not match.")
            return redirect("/signup")

        try:
            if User.objects.get(username=uname):
                messages.info(request, "Username Is Taken")
            return redirect("/signup")
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email Is Taken")
            return redirect("/signup")
        except:
            pass

        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "Signup Successfully! Please Login")
        return redirect("/login")

    return render(request, "signup.html")


def handlelogout(request):
    logout(request)
    messages.info(request, "See You Soon! 😐")
    return redirect("/login")
