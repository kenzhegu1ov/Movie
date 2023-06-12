from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserCreateSerializer
from django.contrib.auth.models import User


# Create your views here.
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            uername=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )
        return Response(data={'user_id': user.id})


@api_view(['POST'])
def authorization_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        """ AUTHENTICATE USER """
        user = authenticate(username=username, password=password)
        """ RETURN TOKEN """
        if user is not None:
            token_, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token_.key})

        """ ERROR """
        return Response(status=status.HTTP_401_UNAUTHORIZED)
