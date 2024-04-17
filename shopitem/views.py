from django.shortcuts import render, redirect
from .models import SecondHandItem, SwapItem
from django.contrib.auth.decorators import login_required


def sell(request):
    # user = request.user

    # selling_items = SecondHandItem.objects.filter(user=user, status='selling')
    # sold_items = SecondHandItem.objects.filter(user=user, status='sold')


    if request.method == 'POST':
        sell_type = request.POST.get('sell_type')

        if sell_type == 'second_hand':
            user = request.user
            name = request.POST.get('name')
            price = request.POST.get('price')
            images = request.FILES.get('image')
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
                images=images,
                status="selling"
            )

            return redirect('home')

        elif sell_type == 'swap':
            user = request.user
            name = request.POST.get('name')
            swapfor = request.POST.get('swapfor')
            images = request.FILES.get('image')
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
                images=images,
                status="swapping"
            )

            return redirect('home')
        
    return render(request, 'sell.html')
    # return render(request, 'sell.html', {
    # 'currently_selling_items': selling_items,
    # 'sold_items': sold_items,
    # })