# textbook/views.py

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, SellItemForm

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