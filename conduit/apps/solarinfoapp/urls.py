from typing import Pattern
from django.conf.urls import url,include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import views
from .views import SolarInfoRetrieveAPIView,SolarInfoViewset, solar_report
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('solar_info', SolarInfoViewset, basename='solar_info')
# router.register('net_meter', net_meter_report, basename='net_meter')

app_name = 'solarinfoapp'
urlpatterns = [
    
    path('solar/info/<str:username>', SolarInfoRetrieveAPIView.as_view()),
    url('', include(router.urls)),
    url('<int:id>/', include(router.urls)),
    path('solar/info', solar_report, name='solar_report'),
]
