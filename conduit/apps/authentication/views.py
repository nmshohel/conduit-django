from conduit.apps.authentication.exceptions import UserDoesNotExist
from conduit.apps.authentication.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required

from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import RegistrationSerializer
from .serializers import (
    LoginSerializer, RegistrationSerializer,UserSerializer,UsersSerializer
)
from .renderers import UserJSONRenderer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request,username, *args, **kwargs):
        
        try:

            user = User.objects.get(username=username)
        except User.DoesNotExist:

            raise UserDoesNotExist
        serializer = self.serializer_class(user)
        # serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        # serializer_data = request.data.get('user', {})
        user_data = request.data.get('user', {})

        serializer_data = {
        'username': user_data.get('username', request.user.username),
        'email': user_data.get('email', request.user.email),

        'profile': {
            'bio': user_data.get('bio', request.user.profile.bio),
            'image': user_data.get('image', request.user.profile.image),
            'office_code': user_data.get('office_code', request.user.profile.office_code),
            'office_name': user_data.get('office_name', request.user.profile.office_name),
            'office_address': user_data.get('office_address', request.user.profile.office_address)
        }
    }

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def userlist(request):
	users = User.objects.all().order_by('-id')
	serializer = UsersSerializer(users, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
@login_required
def userdelete(request, pk):
	task = User.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

# def alluser(self, request, *args, **kwargs):

#     try:

#         user = User.objects.all()
#     except User.DoesNotExist:

#         raise UserDoesNotExist
#     serializer = self.serializer_class(user)
#     # serializer = self.serializer_class(request.user)

#     return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
