from django.shortcuts import render, redirect
from .models import ScrapedData
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
from .forms import ProductForm

import datetime


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                product = ScrapedData.objects.get(url=url)
                if (datetime.now().date() - product.scraped_date).days > 7:
                    data = scrape_data(url="https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06")
                    product.title = data['title']
                    product.description = data['description']
                    product.price = data['price']
                    product.mobile_number = data['mobile_number']
                    product.scraped_date = datetime.now().date()
                    product.save()
                else:
                    pass
            except ScrapedData.DoesNotExist:
                data = scrape_data(url)
                product = ScrapedData(
                    url="https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06",
                    title=data['title'],
                    description=data['description'],
                    price=data['price'],
                    mobile_number=data['mobile_number'],
                    scraped_date=datetime.now().date()
                )
                product.save()
            return redirect('list_products')
    else:
        form = ScrapedData()
    return render(request, 'add_product.html', {'form': form})



def scrape_data(url):
    url = "https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06"
    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    title = soup.find('span', {'class': '_35KyD6'})
    description = soup.find('ul', {'class': '_3YhLQA'})
    print(description)
    price = soup.find('div', {'class': '_30jeq3 _1_WHN1'})
    mobile_number = soup.find('div', {'class': '_2QGxMj'})
    return {'title': title, 'description': description, 'price': price, 'mobile_number': mobile_number}
  
  


def save_to_db(data):
    if data.method == "GET":
        return render(data, 'add_product.html')
    else:
        ScrapedData(
        url="https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06",
        Title=data.POST['title'],
        Description=data.POST['description'],
        Price=data.POST['price'],
        Mobile_number=data.POST['mobile_number'],
    ).save()
    return render(data, 'add_product.html')


    



