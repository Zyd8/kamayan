from django.shortcuts import render, redirect
from .models import SecondHandItem, SwapItem
from django.contrib.auth.decorators import login_required

@login_required
def sell(request):
    if request.method == 'POST':
        sell_type = request.POST.get('sell_type')

        if sell_type == 'second_hand':
            user = request.user
            name = request.POST.get('name')
            price = request.POST.get('price')
            images = request.FILES.getlist('image') 
            description = request.POST.get('description')
            location = request.POST.get('location')
            payment_method = request.POST.get('payment_method')
            pickup_method = request.POST.get('pickup_method')
            category = request.POST.get('category')
            condition = request.POST.get('condition')

            SecondHandItem.objects.create(
                user=user,
                name=name,
                price=price,
                description=description,
                location=location,
                payment_method=payment_method,
                pickup_method=pickup_method,
                category=category,
                condition=condition,
                images=images 
            )

            return redirect('success') 

        elif sell_type == 'swap':
            user = request.user
            name = request.POST.get('name')
            swapfor = request.POST.get('swapfor')
            images = request.FILES.getlist('image')
            description = request.POST.get('description')
            location = request.POST.get('location')
            pickup_method = request.POST.get('pickup_method')
            category = request.POST.get('category')
            condition = request.POST.get('condition')
          

            SwapItem.objects.create(
                user=user,
                name=name,
                swapfor=swapfor,
                description=description,
                location=location,
                pickup_method=pickup_method,
                category=category,
                condition=condition,
                images=images 
            )

            return redirect('success') 

    return render(request, 'sell.html')