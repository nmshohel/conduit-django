from conduit.apps.profiles.models import Profile
from django.urls import path

from .views import ProfileRetrieveAPIView,ProfileAllViewset

app_name = 'profiles'
urlpatterns = [
    path('profiles/<str:username>', ProfileRetrieveAPIView.as_view()),
    path('profile', ProfileAllViewset.as_view()),
]