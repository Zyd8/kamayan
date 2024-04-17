from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shopitem.models import SecondHandItem
from django.contrib.auth.models import Group


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def home(request):
    # Get all second-hand items
    second_hand_items = SecondHandItem.objects.all()

    # Check if the user is a premium member
    is_premium_member = request.user.groups.filter(name='Premium Users').exists()

    # Filter items based on premium membership
    if is_premium_member:
        premium_items = second_hand_items.filter(user__groups__name='Premium Users')
    else:
        premium_items = None

    context = {
        'second_hand_items': second_hand_items,
        'premium_items': premium_items,
        'is_premium_member': is_premium_member
    }

    return render(request, 'home.html', context)

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

def itemroom(request, item_id):
    item = get_object_or_404(SecondHandItem, pk=item_id)
    return render(request, 'itemroom.html', {'item': item})

def become_premium(request):
    if request.user.is_authenticated:
        premium_group, created = Group.objects.get_or_create(name='Premium Users')
        request.user.groups.add(premium_group)
        return redirect('home')
    else:
        return redirect('signin')  
