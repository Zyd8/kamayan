from django.shortcuts import render, redirect, get_object_or_404
from .models import SecondHandItem
from django.contrib.auth.decorators import login_required

@login_required
def sell(request):

    currently_selling_items = SecondHandItem.objects.filter(user=request.user, status="selling")
    sold_items = SecondHandItem.objects.filter(user=request.user, status="sold")

    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        images1 = request.FILES.get('images1')
        images2 = request.FILES.get('images2')
        images3 = request.FILES.get('images3')
        images4 = request.FILES.get('images4')
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
            images1=images1,
            images2=images2,
            images3=images3,
            images4=images4,
            status="selling",
            contacts=contacts,
            swapfor=swapfor,
            isforswap=isforswap, 
        )

        return redirect('home')
     
    return render(request, 'sell.html', {
    'currently_selling_items': currently_selling_items,
    'sold_items': sold_items,
})

@login_required
def update_status(request, item_id):
    item = get_object_or_404(SecondHandItem, pk=item_id)
    if request.user == item.user:  
    
        if item.status == 'selling':
            item.status = 'sold'
        else:
            item.status = 'selling'
        item.save()

    return redirect('sell')
