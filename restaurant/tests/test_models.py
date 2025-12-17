from django.test import TestCase
from restaurant.models import Booking, Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=90, inventory=75)
    
    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Make API request to your endpoint
        client = APIClient()
        response = client.get('/api/menu/')
        
        # Run assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)