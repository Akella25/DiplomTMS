from django.urls import path

from user_authorization.views import registration

urlpatterns = [
    path('registr/', registration, name='registr', )

]
