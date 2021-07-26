import re
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from django.db import models
from .exceptions import ProfileDoesNotExist
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(user__username=username)
        except Profile.DoesNotExist:
            # raise
            raise ProfileDoesNotExist
        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAllViewset(ListAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def get_queryset(self,*args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        # try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.all()
            # profile.office_name
            print(profile)
        # except Profile.DoesNotExist:
        #     # raise
        #     raise ProfileDoesNotExist

            serializer = self.serializer_class(profile)

            return Response(serializer.data, status=status.HTTP_200_OK)