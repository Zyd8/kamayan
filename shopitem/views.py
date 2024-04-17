from django.shortcuts import render, redirect
from .models import SecondHandItem
from django.contrib.auth.decorators import login_required

@login_required
def sell(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        images = request.FILES.get('image')
        description = request.POST.get('description')
        location = request.POST.get('location')
        category = request.POST.get('category')
        condition = request.POST.get('condition')
        contacts = request.POST.get('contacts')
        swapfor = request.POST.get('swapfor')

        sell_type = request.POST.get('sell_type')
        if sell_type == 'second_hand':
            price = request.POST.get('price')
            payment_method = request.POST.get('payment_method')
            isforswap = False
        else:  
            price = 0  
            payment_method = "None"
            isforswap = True

        SecondHandItem.objects.create(
            user=user,
            name=name,
            price=price,
            description=description,
            location=location,
            payment_method=payment_method,  
            category=category,
            condition=condition,
            images=images,
            status="selling",
            contacts=contacts,
            swapfor=swapfor,
            isforswap=isforswap, 
        )

        return redirect('home')
     
    return render(request, 'sell.html')
