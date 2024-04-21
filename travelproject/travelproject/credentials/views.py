from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Login Credentials")
            return redirect("login")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['second_name']
        email = request.POST['email']
        passw = request.POST['password']
        cpass = request.POST['password1']
        if passw == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,password=passw,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('/')
                print("User Created")
        else:
            messages.info(request,"password not matching")
            return register("register")
        return register("/")
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")