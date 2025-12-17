
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'booking', views.bookingViewSet, basename='booking')

urlpatterns = [ 
    path('menu/', views.menuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.singleMenuItemView.as_view(), name='single-menu-item'),
    path('', include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]