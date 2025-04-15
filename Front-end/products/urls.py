app_name="products"
from django.urls import path

from .views import index, product_detail,product_show,about,contact,signup,login,add_product
urlpatterns = [
    path('', index, name='index'), # URL pattern for the index view
    path('products/<str:slug>/', product_detail, name='product_detail'), # URL pattern for the product detail view
    path('products/', product_show, name='product_list'), # URL pattern for the product list view
    path('about/', about, name='about'), # URL pattern for the about view
    path('contact/', contact, name='contact'), # URL pattern for the contact view
    path('signup',signup,name="signup"),
    path('login',login,name="login"), # URL pattern for the login view
    path('add_product',add_product,name="add_product")
]
