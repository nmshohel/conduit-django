from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,viewsets,mixins
from rest_framework import response
from conduit.apps.authentication.renderers import UserJSONRenderer
from conduit.apps.authentication.models import User
from datetime import date
from rest_framework import status
from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
from requests.structures import CaseInsensitiveDict
from django.shortcuts import render,HttpResponse,redirect
from rest_framework.serializers import Serializer
from .exceptions import NetMeterDoesNotExist
from .models import NetMeterInfo
from .renderers import NetMeterJSONRenderer
from .serializers import NetMeterInfoSerializer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

class NetMeterInfoRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (NetMeterJSONRenderer,)
    serializer_class = NetMeterInfoSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            netmeterinfo = NetMeterInfo.objects.select_related('user').get(
                user__username=username
            )
        except NetMeterDoesNotExist:
            # raise
            raise NetMeterDoesNotExist
        serializer = self.serializer_class(netmeterinfo)

        return Response(serializer.data, status=status.HTTP_200_OK)
#--------------------------------------------------------------#

class NetMeterInfoViewset(viewsets.ModelViewSet):
    serializer_class = NetMeterInfoSerializer
    # throttle_scope = "first_app"
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        net_meter_info = NetMeterInfo.objects.all()
        return net_meter_info

   
    def create(self, request, *args, **kwargs):
        meter_data = request.data

        new_info = NetMeterInfo.objects.create(install_meter_nos=meter_data["install_meter_nos"], capacity_of_install_meter=meter_data[
            "capacity_of_install_meter"], month=meter_data["month"],year=meter_data["year"], fy=meter_data["fy"],office_code=meter_data["office_code"])

        new_info.save()

        serializer = NetMeterInfoSerializer(new_info)

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
        net_meter_object = self.get_object()
        data = request.data

        # car_plan = NetMeterInfo.objects.get(plan_name=data["plan_name"])

        # car_object.car_plan = car_plan
        net_meter_object.install_meter_nos = data["install_meter_nos"]
        net_meter_object.capacity_of_install_meter = data["capacity_of_install_meter"]
        net_meter_object.month = data["month"]
        net_meter_object.year = data["year"]
        net_meter_object.fy = data["fy"]
        net_meter_object.office_code = data["office_code"]

        net_meter_object.save()

        serializer = NetMeterInfoSerializer(net_meter_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        net_meter_object = self.get_object()
        data = request.data

        # try:
        #     # car_plan = NetMeterInfo.objects.get(plan_name=data["plan_name"])
        #     car_object.car_plan = car_plan
        # except KeyError:
        #     pass

        net_meter_object.install_meter_nos = data.get("install_meter_nos", net_meter_object.install_meter_nos)
        net_meter_object.capacity_of_install_meter = data.get("capacity_of_install_meter", net_meter_object.capacity_of_install_meter)
        net_meter_object.month = data.get("month", net_meter_object.month)
        net_meter_object.year = data.get("year", net_meter_object.year)
        net_meter_object.fy = data.get("fy", net_meter_object.fy)
        net_meter_object.office_code = data.get("office_code", net_meter_object.office_code)

        net_meter_object.save()

        serializer = NetMeterInfoSerializer(net_meter_object)

        return Response(serializer.data)
# #--------------------------------------------------#
# class NetMeterPostView(ListCreateAPIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (NetMeterJSONRenderer,)
#     serializer_class = NetMeterInfoSerializer
    # @csrf_exempt
    # def create(self, validated_data):
    #     serializer=self.get_serializer(data=self.request.data)
    #     user_id_for_netmeterinfo=self.request.data.pop('User_id')
    #     user_instance=User.objects.filter(id=user_id_for_netmeterinfo).first()
    #     if not serializer.is_valid():
    #         serializer.errors
    #     data=serializer.validated_data
    #     serializer.save(user=user_instance)
    #     headers=self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)
# #----------------------------------------------------#
#     def post(self, request):
#         netmeterinfo=request.data.get('netmeterinfo',{})
#         print("This is 2:",netmeterinfo)
#         serializer=self.serializer_class(data=netmeterinfo)
#         # serializer = NetMeterInfoSerializer(data=request.data)
#         print("This is 3:",serializer)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def net_meter_report(request):
    response=requests.get('http://127.0.0.1:8000/api/net_meter_info/').json()
    return render(request,'net_meter_report.html',{'response':response})
    

# , params=request.POST
def index(request):

    return render(request, 'index.html')
# -------------- Normal Login-------------
# def user_login(request):
#     if request.method=='POST':
#         username=request.POST.get('uname1')
#         password=request.POST.get('pwd1')
#         user=authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
            
#             return redirect ('/api/index')
#         else:
#             messages.info(request, 'Username or Password is Incorrect')
#             return render(request, 'user_login.html')
#     context={}
#     return render(request, 'user_login.html',context)
#-------------------------------------

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('uname1')
        password=request.POST.get('pwd1')
        # response=requests.post('http://127.0.0.1:8000/api/users/login').json()
        query = {'email':'ripon@gmail.com', 'password':'Ripon@123'}
        response = requests.post('http://127.0.0.1:8000/api/users/login', json=query)
        print(response.json())
        # return redirect ('/api/index')
        # else:
        #     messages.info(request, 'Username or Password is Incorrect')
        #     return render(request, 'user_login.html')
    context={}
    return render(request, 'user_login.html',context)


def user_logout(request):
    return render(request, 'user_login.html')


