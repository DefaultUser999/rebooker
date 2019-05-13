# users/urls.py
#Reference https://academy.muva.tech/blog/?s=Django+2.
from django.urls import path, re_path
from . import views


app_name='textbook'

urlpatterns = [
    path('product/detail/<int:id>/', views.product_detail, name='detail'),
    path('products/', views.products, name='products' ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]