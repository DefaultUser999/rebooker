# textbook/views.py

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, SellItemForm, BuyItemForm

from .models import Item

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# /textbook/sell
def sell(request):
    template_name = 'sell.html'
    if request.method == "POST":
        my_form = SellItemForm(request.POST)
        if my_form.is_valid() :
            item = my_form.save(commit=False)
            item.seller = request.user
            item.save()
            print(my_form)
            print(item)
            messages.success(request, 'Item has be placed for sale with success!')
            return redirect('sell')
        else :
            messages.error(request, 'Ops! Something went wrong')
        return redirect('sell')

    my_form  = SellItemForm(request.GET)

    context = {
        "form" : my_form
    }
    return render(request, 'sell.html', context)

#  TODO: Buy View
#  need to load in the item which we want to buy,
#  the user logged in, as they will be the buyer
#  and update the item information of submission of the form
#  ie: POST

# /textbook/buy/item_id
def buy(request, item_id):
    template_name = 'buy.html'
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "GET":
        form = BuyItemForm(request.GET)
    elif request.method == "POST":
        form = BuyItemForm(request.POST)
        if form.is_valid() :
            item.buyer = request.user
            item.status_sold=True
            item.save()
            messages.success(request, 'Item has been purchased with success!')
            return redirect('home')
        else :
            messages.error(request, 'Ops! Something went wrong')
        return redirect('buy')

    context = {
        'item' : item,
        'form' : form
    }
    return render(request, 'buy.html', context)
