from django.conf.urls import url
from django.urls import path


from .views import (
    LoginAPIView, RegistrationAPIView, PbsUserRetrieveUpdateAPIView, userdelete, pbsuserlist,
rebuserlist,)

app_name = 'authentication'
urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('pbsusers',pbsuserlist, name='pbsuserlist'),
    path('rebusers',rebuserlist, name='rebuserlist'),
    path('user/<str:username>', PbsUserRetrieveUpdateAPIView.as_view()),
    path('user/<str:pk>/', userdelete, name="userdelete"),
  
]
