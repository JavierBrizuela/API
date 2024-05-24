from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializers import UserCreateSerializer, UserUpdateSerializer, ChangePasswordSerializer

@extend_schema(
    description='Create new user',
    summary='User',
    request=UserCreateSerializer,
    responses={201:UserCreateSerializer},
)
class SignUpView(CreateAPIView):
        
    serializer_class = UserCreateSerializer

@extend_schema(
    description='Update user',
    summary='User',
    request=UserUpdateSerializer,
    responses={200:UserUpdateSerializer},
)    
class ProfileView(RetrieveUpdateAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = UserUpdateSerializer
    http_method_names = ['get', 'patch']
    
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user 

@extend_schema(
    description='Change password',
    summary='User'
    )    
class ChangePasswordView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer
    http_method_names = ['put',]
    
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user        
    
    def put(self, request):
        
        serializer = self.serializer_class(data=request.data, context={'user':request.user})
        if serializer.is_valid():
            user = request.user
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            user.save()
            return Response(
                {'message':'contraseña actualizada'}, status=status.HTTP_200_OK
            )
        return Response(
            {'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )