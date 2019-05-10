from django.shortcuts import render

# Create your views here.


# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
def About(request):
    template_name = 'about.html'
    return render(request, 'about.html')
    
def Cart(request):
    template_name = 'cart.html'
    return render(request, 'cart.html')
    
def Checkout(request):
    template_name = 'checkout.html'
    return render(request, 'checkout.html')
    
def Contact(request):
    template_name = 'contact.html'
    return render(request, 'contact.html')
    
def Featured(request):
    template_name = 'featured.html'
    return render(request, 'featured.html')
    
def Index(request):
    template_name = 'index.html'
    return render(request, 'index.html')

def OrderComplete(request):
    template_name = 'order-complete.html'
    return render(request, 'order-complete.html')
    
def ProductDetail(request):
    template_name = 'product-detail.html'
    return render(request, 'product-detail.html')
    
    
    
    
    
    
    