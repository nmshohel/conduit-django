from typing import Pattern
from django.conf.urls import url,include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import views
from .views import NetMeterInfoRetrieveAPIView,NetMeterInfoViewset, net_meter_report,index,user_login,user_logout
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('net_meter_info', NetMeterInfoViewset, basename='net_meter_info')
# router.register('net_meter', net_meter_report, basename='net_meter')

app_name = 'rebpbsinfoapp'
urlpatterns = [
    
    path('rebpbsinfoapp/<str:username>', NetMeterInfoRetrieveAPIView.as_view()),
    # path('rebpbsinfoapp/netmeterinfo', NetMeterInfoViewset, name='nmtr'),
    url('', include(router.urls)),
    url('<int:id>/', include(router.urls)),
    path('net_meter/', net_meter_report, name='net_meter_report'),
    # url(r'netmeterinfo/$', csrf_exempt(NetMeterPostView)),
    path('index/', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    # path('monthly-report/', monthly_report, name='monthly_report'),
    # path('net_meter_info/', net_meter_info, name='net_meter_info'),
]
