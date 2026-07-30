from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import Registerform

# Create your views here.
def register(request):
    if request.method == "POST":
        form = Registerform(request.POST)

        if form.is_valid():
            print("✅ Form Valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("✅ User Saved")
            messages.success(request,"Registration successful.")
            return redirect("login")
    else:
        form = Registerform()

    return render(request,"accounts/register.html",{"form":form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request,"accounts/login.html",)

def logout_view(request):
    logout(request)
    return redirect("login")
