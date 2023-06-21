from django.test import TestCase
from .models import Shop
from django.contrib.gis.geos import Point

# Create your tests here.

class TestCalls(TestCase):
    def setUp(self):
        shop1 = Shop.objects.create(name="Test1", address="Address1", city="City 1", location=Point(23.123,23.123))
        shop2 = Shop.objects.create(name="Test2", address="Address2", city="City 2", location=Point(23.124,23.124))
        self.shop1 = shop1
        self.shop2 = shop2

    def test_home_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_detail_view(self):
        response = self.client.get(f'/detail/{self.shop1.pk}')
        self.assertTemplateUsed(response, 'detail.html')

    def test_update_view(self):
        response = self.client.get(f'/update/{self.shop1.pk}')
        self.assertTemplateUsed(response, 'update.html')

    def test_delete_view(self):
        response = self.client.get(f'/delete/{self.shop1.pk}')
        self.assertTemplateUsed(response, 'delete.html')

    def test_shop_list_view(self):
        response = self.client.get('/shop_list/')
        self.assertTemplateUsed(response, 'shop_list.html')

    def test_home_post_view(self):
        response = self.client.post('/', {"name": "Test", "location": "POINT(23,23)"})
        self.assertTemplateUsed(response, 'home.html')

    def test_delete_post_view(self):
        response = self.client.post(f'/delete/{self.shop1.pk}', {"name": "Test", "location": "POINT(123,123)"})
        self.assertRedirects(response, '/')

    def test_shop_list_post_view(self):
        response = self.client.post('/shop_list/', {"longitude":23.124,"latitude":23.124,"distance":5})
        self.assertTemplateUsed(response, 'shop_list.html')
        self.assertNotContains(response=response, text="No shops")