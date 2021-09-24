from django.conf.urls import url
from django.urls import path


from .views import (
    LoginAPIView, RegistrationAPIView, SuperUserRegistrationAPIView,
    PbsUserRetrieveUpdateAPIView,RebUserRetrieveUpdateAPIView,userdelete,
    pbsuserlist,rebuserlist,)

app_name = 'authentication'
urlpatterns = [
    path('superuserregister/', SuperUserRegistrationAPIView.as_view()), 
    # New Registerd user should be inactive, It need Active by Admin user
    path('register/', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('pbsusers',pbsuserlist, name='pbsuserlist'),
    path('rebusers',rebuserlist, name='rebuserlist'),
    path('pbsuser/<str:username>', PbsUserRetrieveUpdateAPIView.as_view()),
    path('rebuser/<str:username>', RebUserRetrieveUpdateAPIView.as_view()),
    path('user/<str:username>', userdelete, name="userdelete"),
  
]
