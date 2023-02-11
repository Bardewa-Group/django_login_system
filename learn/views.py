from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    
def loginUser(request):
    # checking if the user has entered the valid credintials
    if request.method == "POST":
        username = request.POST.get('username_data')
        password = request.POST.get('password_data')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

