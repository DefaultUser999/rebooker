from django.urls import path, re_path
from . import views

app_name='textbook'

urlpatterns = [
    path('product/detail/<int:id>/', views.product_detail, name='detail'),
    path('products/', views.products, name='products' ),
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
    path('transaction-history/', views.transaction_history, name='transaction-history'),
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]