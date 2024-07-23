from django.urls import path

from user_authorization.views import registration, log_in, log_out, info_user, book_room_form, book_room, del_booking

urlpatterns = [
    path('registr/', registration, name='registr'),
    path('log_in/', log_in, name='log_in'),
    path('log_aut', log_out, name='log_out'),
    path('info_user', info_user, name='info_user'),
    path('booking/<int:pk>', book_room_form, name='booking'),
    path('booking', book_room, name='book_room'),
    path('booking_del/<int:pk>', del_booking, name='del_booking')

]
