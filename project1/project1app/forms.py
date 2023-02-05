from django import forms
from .models import ScrapedData
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

CATEGORY_CHOICES = [    ('name', 'name'),    ('value', 'value'),]

class ProductForm(forms.Form):
    url = forms.URLField(label='URL')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    url = "https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06"
    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    title = soup.find('span', {'class': '_35KyD6'})
    description = soup.find('ul', {'class': '_3YhLQA'})
    price = soup.find('div', {'class': '_30jeq3 _1_WHN1'})
    images = soup.find('div',{'class="_3kidJX"'})
    mobile_number = soup.find('div', {'class': '_2QGxMj'})
    print(mobile_number)
        # return {'title': title, 'description': description, 'price': price, 'mobile_number': mobile_number}

    title='SRPM Wayfarer Sunglasses'
    description='Stylish and comfortable sunglasses'
    price=499.0
    mobile_number='9876543210'
    size='Medium'
    images=images

def list_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            products = ScrapedData.objects.filter(category=category)
    else:
        form = ProductForm()
        products = ScrapedData.objects.all()
    return render(request, 'add_product.html', {'form': form, 'products': products})
