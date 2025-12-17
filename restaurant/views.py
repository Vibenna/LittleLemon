from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


class menuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class bookingView(APIView):
    
#     def get(self, request):
#         bookings = Booking.objects.all()
#         serializer = bookingSerializer(bookings, many=True)
#         return Response(serializer.data)

# class menuItmeView(APIView):
    
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = menuSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# # def sayHello(request):
# #     return HttpResponse("Hello from the Little Lemon Restaurant!")

# # Create your views here.
# def index(request):
#     return render(request, 'index.html', {})

