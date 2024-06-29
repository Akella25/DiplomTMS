from django.urls import path

from user_authorization.views import registration, log_in, log_out

urlpatterns = [
    path('registr/', registration, name='registr', ),
    path('log_in/', log_in, name='log_in'),
    path('log_aut', log_out, name='log_out')

]
