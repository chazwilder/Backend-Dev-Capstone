from .views import BookingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)