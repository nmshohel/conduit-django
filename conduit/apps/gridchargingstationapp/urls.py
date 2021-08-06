from typing import Pattern
from django.conf.urls import url,include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import views
from .views import GridChargingStationInfoRetrieveAPIView,GridChargingStationInfoViewset, grid_charging_station_report
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('gridchargingstation_info', GridChargingStationInfoViewset, basename='gridchargingstation_info')
# router.register('net_meter', net_meter_report, basename='net_meter')

app_name = 'gridchargingstationapp'
urlpatterns = [
    
    path('grid-charging-station/info/<str:username>', GridChargingStationInfoRetrieveAPIView.as_view()),
    url('', include(router.urls)),
    url('<int:id>/', include(router.urls)),
    path('grid-charging-station/info', grid_charging_station_report, name='grid_charging_station_report'),
]