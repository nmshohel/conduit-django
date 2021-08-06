from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,viewsets
from rest_framework import response
from conduit.apps.authentication.renderers import UserJSONRenderer
from conduit.apps.authentication.models import User
from datetime import date
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
from requests.structures import CaseInsensitiveDict
from django.shortcuts import render,HttpResponse,redirect
from rest_framework.serializers import Serializer
from .exceptions import GridChargingStationDoesNotExist
from .models import GridChargingStationInfo
from .renderers import GridChargingStationJSONRenderer
from .serializers import GridChargingStationInfoSerializer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

class GridChargingStationInfoRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (GridChargingStationJSONRenderer,)
    serializer_class = GridChargingStationInfoSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            gridchargingstationinfo = GridChargingStationInfo.objects.select_related('user').get(
                user__username=username
            )
        except GridChargingStationDoesNotExist:
            # raise
            raise GridChargingStationDoesNotExist
        serializer = self.serializer_class(gridchargingstationinfo)

        return Response(serializer.data, status=status.HTTP_200_OK)
#--------------------------------------------------------------#

class GridChargingStationInfoViewset(viewsets.ModelViewSet):
    serializer_class = GridChargingStationInfoSerializer
    # throttle_scope = "first_app"
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        gridchargingstationinfo = GridChargingStationInfo.objects.all()
        return gridchargingstationinfo

   
    def create(self, request, *args, **kwargs):
        charging_data = request.data

        new_info = GridChargingStationInfo.objects.create(charging_station_nos=charging_data["charging_station_nos"], charging_station_capacity=charging_data[
            "charging_station_capacity"], month=charging_data["month"],year=charging_data["year"], fy=charging_data["fy"],pbs_code=charging_data["pbs_code"])

        new_info.save()

        serializer = GridChargingStationInfoSerializer(new_info)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            car = self.get_object()
            car.delete()
            response_message = {"message": "Item has been deleted"}
        else:
            response_message = {"message": "Not Allowed"}

        return Response(response_message)

    def update(self, request, *args, **kwargs):
        grid_cgg_stn_object = self.get_object()
        data = request.data

        grid_cgg_stn_object.charging_station_nos = data["charging_station_nos"]
        grid_cgg_stn_object.charging_station_capacity = data["charging_station_capacity"]
        grid_cgg_stn_object.month = data["month"]
        grid_cgg_stn_object.year = data["year"]
        grid_cgg_stn_object.fy = data["fy"]
        grid_cgg_stn_object.pbs_code = data["pbs_code"]

        grid_cgg_stn_object.save()

        serializer = GridChargingStationInfoSerializer(grid_cgg_stn_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        grid_cgg_stn_object = self.get_object()
        data = request.data


        grid_cgg_stn_object.charging_station_nos = data.get("charging_station_nos", grid_cgg_stn_object.charging_station_nos)
        grid_cgg_stn_object.charging_station_capacity = data.get("charging_station_capacity", grid_cgg_stn_object.charging_station_capacity)
        grid_cgg_stn_object.month = data.get("month", grid_cgg_stn_object.month)
        grid_cgg_stn_object.year = data.get("year", grid_cgg_stn_object.year)
        grid_cgg_stn_object.fy = data.get("fy", grid_cgg_stn_object.fy)
        grid_cgg_stn_object.pbs_code = data.get("pbs_code", grid_cgg_stn_object.pbs_code)

        grid_cgg_stn_object.save()

        serializer = GridChargingStationInfoSerializer(grid_cgg_stn_object)

        return Response(serializer.data)



def grid_charging_station_report(request):
    response=requests.get('http://127.0.0.1:8000/api/gridchargingstation_info/').json()
    return render(request,'grid_charging_station_report.html',{'response':response})
    



