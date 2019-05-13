from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
#Reference https://academy.muva.tech/blog/?s=Django+2.
# Create your views here.


# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

from .models import Product

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'list.html', context)


def product_detail(request, id, slug):
    template_name='detail.html'
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)

def products(request):
    template_name='products.html'
    products= Product.objects.all()
    print(products)
    context = {
        "products": products,
    }
    return render(request, 'products.html', context)