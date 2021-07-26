from django.conf.urls import url
from django.urls import path,include
# from django.contrib import admin

# from .views import RegistrationAPIView,LoginAPIView
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, userdelete,userlist
)

app_name = 'authentication'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('conduit.apps.authentication.urls', namespace='authentication')),
    path('register/', RegistrationAPIView.as_view()),
    # url(r'^users/?$', RegistrationAPIView.as_view()),
    # url(r'^users/login/?$', LoginAPIView.as_view()),

    # path('user', UserRetrieveUpdateAPIView.as_view()),
    path('user/<str:username>', UserRetrieveUpdateAPIView.as_view()),

    path('user/<str:pk>/', userdelete, name="userdelete"),
    path('users',userlist, name='userlist'),
    path('login', LoginAPIView.as_view()),
    
]
# urlpatterns = [
#     url(r'^users/?$', RegistrationAPIView.as_view()),
#     url(r'^users/login/?$', LoginAPIView.as_view()),
# ]