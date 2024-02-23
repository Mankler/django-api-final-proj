from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_create_menu_item(self):
        menu_item =  Menu.objects.create(title="French Fries", price=100.99, inventory=2)
        self.assertEqual(str(menu_item), "French Fries : 100.99")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="French Fries", price=100.99, inventory=2)
        Menu.objects.create(title="Hamburger", price=10.99, inventory=20)

    def test_getall(self):
        french_fries = Menu.objects.get(title="French Fries")
        hamburger = Menu.objects.get(title="Hamburger")
        self.assertEqual(str(french_fries), "French Fries : 100.99")
        self.assertEqual(str(hamburger), "Hamburger : 10.99")
