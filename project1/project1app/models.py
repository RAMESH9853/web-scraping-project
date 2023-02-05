from django.db import models

class ScrapedData(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    mobile_number = models.CharField(max_length=15)
    size = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    product_images = models.ImageField(upload_to='product_images')