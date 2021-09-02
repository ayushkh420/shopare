from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching.')
            return redirect('register')
        return redirect('/')


    else:
        return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/accounts/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")


    else:
        return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect("/")

def home(request):
    return render(request, 'home.html')

def grocery(request):
    return render(request, 'grocery.html')


