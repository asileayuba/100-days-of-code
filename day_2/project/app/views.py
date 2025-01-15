from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact, Blogs

# This imports below is for sending emails
from django.conf import settings
from django.core.mail import send_mail
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

        # Save contact query to the database
        query = Contact(name=fname, email=femail, phoneNumber=phone, description=desc)
        query.save()

        # Email configuration for sending to the host
        from_email = settings.EMAIL_HOST_USER
        recipient_email = "asileayuba@gmail.com"
        subject = f"Query from {fname}"
        body = (
            f"User Email: {femail}\n"
            f"User Phone Number: {phone}\n\n"
            f"Query:\n{desc}"
        )

        try:
            # Send email to the host
            email_message = EmailMessage(subject, body, from_email, [recipient_email])
            email_message.send(fail_silently=False)

            # Send confirmation email to the sender
            confirmation_subject = "Thank You for Reaching Out"
            confirmation_body = (
                f"Hello {fname},\n\n"
                "Thank you for your message! \nWe've received your inquiry and will respond to you shortly.\n\n"
                "Best Regards,\nAsile Ayuba."
            )
            send_mail(
                confirmation_subject, 
                confirmation_body, 
                from_email, 
                [femail], 
                fail_silently=False
            )

            messages.success(
                request, "Thank you for reaching out! We'll get back to you shortly."
            )
        except Exception as e:
            messages.error(
                request, f"Something went wrong while sending your email: {e}"
            )
            return redirect("/contact")

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


def handleBlog(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login to view the Blog Post")
        return redirect("/login")
    allPosts=Blogs.objects.all()
    context={'allPosts': allPosts}
    print(allPosts)
    return render(request, 'blog.html', context)

def search(request):
    query=request.GET['search']
    if len(query)>100:
        allPosts=Blogs.objects.none()
    else:
        allPostsTitle=Blogs.objects.filter(title__icontains=query)
        allPostsDescription=Blogs.objects.filter(description__icontains=query)
        allPosts=allPostsTitle.union(allPostsDescription)
    if allPosts.counts()==0:
        messages.warning(request, "No Search Results")
    params={"allPosts":allPosts, "query":query}
    
    return render(request, "search.html", params)