from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})
# class Menu():
@api_view(['GET','POST'])
def MenuItemsView(request):
    queryset = Menu.objects.all()
    serialized = MenuSerializer(queryset, many=True)
    return Response(serialized.data)
    


@api_view(['GET','PUT','DELETE'])
def SingleMenuItemView(request,pk):
    queryset = Menu.objects.get(pk=pk)
    serialized = MenuSerializer(queryset)
    return Response(serialized.data)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
