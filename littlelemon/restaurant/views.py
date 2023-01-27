from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})
# class Menu():
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def MenuItemsView(request):
    if request.method == 'GET':
        queryset = Menu.objects.all()
        serialized = MenuSerializer(queryset, many=True)
        return Response(serialized.data)
    if request.method == 'POST':
        serialized = MenuSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({"Details":"Menu item successfully created!","data":serialized.data})
        else:
            return Response({"Details":"Invalid Data Sent"})
            
    

@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def SingleMenuItemView(request,pk):
    queryset = get_object_or_404(Menu, pk=pk)
    if request.method == 'GET':
        serialized = MenuSerializer(queryset)
        return Response(serialized.data)
    if request.method == 'PUT':
        serialized = MenuSerializer(data=request.data)
        if serialized.is_valid():
            queryset.Title = serialized.data['Title']
            queryset.Price = serialized.data['Price']
            queryset.Inventory = serialized.data['Inventory']
            queryset.save()
        else:
            print(serialized.errors)
            
        return Response({"Details":"Menu item has been successfully updated! ","data":serialized.data})
    if request.method == 'DELETE':
        queryset.delete()
        return Response("Menu item has been successfully deleted!")


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
