from typing import Pattern
from django.conf.urls import url,include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import views
from .views import NetMeterInfoRetrieveAPIView,NetMeterInfoViewset, net_meter_report
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('net_meter_info', NetMeterInfoViewset, basename='net_meter_info')
# router.register('net_meter', net_meter_report, basename='net_meter')

app_name = 'rebpbsinfoapp'
urlpatterns = [
    
    path('rebpbsinfoapp/<str:username>', NetMeterInfoRetrieveAPIView.as_view()),
    url('', include(router.urls)),
    url('<int:id>/', include(router.urls)),
    path('net_meter/', net_meter_report, name='net_meter_report'),

]
