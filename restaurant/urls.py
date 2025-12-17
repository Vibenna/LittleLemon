from django.contrib import admin 
from django.urls import path 
from . import views


urlpatterns = [ 
    # path('', views.sayHello, name='sayHello'), 
    # path('', views.index, name='index'),
    path('menu/', views.menuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.singleMenuItemView.as_view(), name='single-menu-item'),
    # path('booking/', views.bookingView.as_view(), name='bookings'),
]