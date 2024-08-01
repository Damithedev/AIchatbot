from django.urls import path

from ChatbotAPI.views import Registeruser, ListUsers, Loginview, SendMessage, Checktoken

urlpatterns = [
    path('users/', ListUsers.as_view(), name='register'),
    path('users/register/', Registeruser.as_view(), name='register'),
    path('users/login/', Loginview.as_view(), name='login'),
    path('send/', SendMessage.as_view(), name='send'),
    path('token/', Checktoken.as_view(), name='token')

]
