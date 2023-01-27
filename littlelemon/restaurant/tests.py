from django.test import TestCase
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from .views import MenuItemsView,BookingViewSet

#TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.cParm = Menu.objects.create(Title="Chicken Parm",Price=12,Inventory=100)
        self.cParm = Menu.objects.create(Title="Fried Fish",Price=16,Inventory=50)
        
    def test_getall(self):
        menuItems = Menu.objects.all()
        serialized = MenuSerializer(menuItems,many=True)
        print(str(serialized.data))
        self.assertEquals(str(serialized.data), "[OrderedDict([('ID', 2), ('Title', 'Chicken Parm'), ('Price', '12.00'), ('Inventory', 100)]), OrderedDict([('ID', 3), ('Title', 'Fried Fish'), ('Price', '16.00'), ('Inventory', 50)])]")
    

        
