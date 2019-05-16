from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, SellItemForm, BuyItemForm
from .models import Item, Product, Category

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# /textbook/sell
@login_required
def sell(request):
    template_name = 'sell.html'
    if request.method == "POST":
        my_form = SellItemForm(request.POST)
        if my_form.is_valid() :
            item = my_form.save(commit=False)
            item.seller = request.user
            item.save()

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

# /textbook/buy/item_id
@login_required
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

@login_required
def transaction_history(request):
    template_name = 'transaction_history.html'
    user = request.user
    items_purchased = Item.objects.filter(buyer=user)
    items_sold = Item.objects.filter(seller=user)
    
    context = {
        'user' : user,
        'items_purchased': items_purchased,
        'items_sold': items_sold
    }
    return render(request, 'transaction_history.html', context)

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

def ProductDetail(request):
    template_name = 'product-detail.html'
    return render(request, 'product-detail.html')

def products(request):
    template_name='products.html'
    products= Product.objects.all()
    print(products)
    context = {
        "products": products,
    }
    return render(request, 'products.html', context)

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