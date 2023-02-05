from django.test import TestCase
from .models import ScrapedData

class ScrapedDataTestCase(TestCase):
    def test_scraped_data_model(self):
        scraped_data = ScrapedData.objects.create(
            url="https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06",
            title="SRPM Wayfarer Sunglasses",
            description="Elevate your style quotient with these stylish wayfarer sunglasses",
            price=999,
            mobile_number="9876543210"
        )
        self.assertEqual(scraped_data.title, "SRPM Wayfarer Sunglasses")
        self.assertEqual(scraped_data.price, 999)

