from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        if not all([username, password, confirm_password]):
            return render(request, 'signup.html', {'error_message': 'All fields are required'})
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('home') 

    else:
        return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('home')
