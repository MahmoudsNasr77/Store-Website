from django.http import Http404
from django.shortcuts import render
import requests

from django_countries import countries

def fetch_products_from_api(request):
    name = request.GET.get('name', '')
    price = request.GET.get('price', '')
    order_by = request.GET.get('order_by', '')
    page = int(request.GET.get('page', 1))
    api_url = 'http://127.0.0.1:8000/api/product_search'

    params = {
        'name': name,
        'price': price,
        'ordering': order_by,
        'page': page,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    return {
        'products': data.get('results', []),
        'prev_page': data.get('previous', None),
        'next_page': data.get('next', None),
        'name': name,
        'price': price,
        'ordering': order_by,
        'current_page': page,
    }


def index(request):
    context = fetch_products_from_api(request)

    return render(request, 'index.html', context)   
def product_detail(request, slug):
    # Construct the API URL to get the product detail
    api_url = f'http://127.0.0.1:8000/api/products/{slug}/'  # API endpoint for a single product
    response = requests.get(api_url)

    if response.status_code == 200:
        product = response.json()  # Get the product data as JSON
    else:
        raise Http404("Product not found")  # Raise 404 if product is not found

    return render(request, 'product_detail.html', {'product': product})


def product_show(request):
    context = fetch_products_from_api(request)
    return render(request, 'products.html', context)
def about(request):
    return render(request, 'about.html')  # Render the about page template
def contact(request):       
    return render(request, 'contactus.html')  # Render the contact page template
def signup(request):
    countries_list = countries

    return render(request,'signup.html',{'countries_list': countries_list})  # Render the signup page template

def login(request):
    return render(request, 'login.html')  # Render the login page template
def add_product(request):
  
    return render(request, 'add_product.html')  # Render the add product page template