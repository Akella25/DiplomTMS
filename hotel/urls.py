from django.urls import path
from hotel.views import hotel_info, search_hotel


urlpatterns = [
    path('info/<int:pk>/', hotel_info, name='info'),
    path('search/', search_hotel, name='search')


]