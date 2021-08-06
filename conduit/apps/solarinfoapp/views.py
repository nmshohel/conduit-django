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
from .exceptions import SolarDoesNotExist
from .models import SolarPanelInfo
from .renderers import SolarJSONRenderer
from .serializers import SolarInfoSerializer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

class SolarInfoRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (SolarJSONRenderer,)
    serializer_class = SolarInfoSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            solarinfo = SolarPanelInfo.objects.select_related('user').get(
                user__username=username
            )
        except SolarDoesNotExist:
            # raise
            raise SolarDoesNotExist
        serializer = self.serializer_class(solarinfo)

        return Response(serializer.data, status=status.HTTP_200_OK)
#--------------------------------------------------------------#

class SolarInfoViewset(viewsets.ModelViewSet):
    serializer_class = SolarInfoSerializer
    # throttle_scope = "first_app"
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        solar_info = SolarPanelInfo.objects.all()
        return solar_info

   
    def create(self, request, *args, **kwargs):
        solar_data = request.data

        new_info = SolarPanelInfo.objects.create(last_month_solar_panel_consumer_nos=solar_data["last_month_solar_panel_consumer_nos"], last_month_solar_panel_capacity=solar_data[
            "last_month_solar_panel_capacity"], month=solar_data["month"],year=solar_data["year"], fy=solar_data["fy"],pbs_code=solar_data["pbs_code"])

        new_info.save()

        serializer = SolarInfoSerializer(new_info)

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
        solar_object = self.get_object()
        data = request.data

        solar_object.last_month_solar_panel_consumer_nos = data["last_month_solar_panel_consumer_nos"]
        solar_object.last_month_solar_panel_capacity = data["last_month_solar_panel_capacity"]
        solar_object.month = data["month"]
        solar_object.year = data["year"]
        solar_object.fy = data["fy"]
        solar_object.pbs_code = data["pbs_code"]

        solar_object.save()

        serializer = SolarInfoSerializer(solar_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        solar_object = self.get_object()
        data = request.data


        solar_object.last_month_solar_panel_consumer_nos = data.get("last_month_solar_panel_consumer_nos", solar_object.last_month_solar_panel_consumer_nos)
        solar_object.last_month_solar_panel_capacity = data.get("last_month_solar_panel_capacity", solar_object.last_month_solar_panel_capacity)
        solar_object.month = data.get("month", solar_object.month)
        solar_object.year = data.get("year", solar_object.year)
        solar_object.fy = data.get("fy", solar_object.fy)
        solar_object.pbs_code = data.get("pbs_code", solar_object.pbs_code)

        solar_object.save()

        serializer = SolarInfoSerializer(solar_object)

        return Response(serializer.data)



def solar_report(request):
    response=requests.get('http://127.0.0.1:8000/api/solar_info/').json()
    return render(request,'solar_report.html',{'response':response})
    



