# textbook/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('about/', views.About, name='about'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('contact/', views.Contact, name='contact'),
    path('featured/', views.Featured, name='featured'),
    path('index/', views.Index, name='index'),
    path('order-complete/', views.OrderComplete, name='order-complete'),
    path('product-detail/', views.ProductDetail, name='product-detail'),
    path('sell/', views.sell, name='sell'),
    path('buy/<int:item_id>/', views.buy, name='buy'),
    path('transaction-history/', views.transaction_history, name='transaction-history')
]