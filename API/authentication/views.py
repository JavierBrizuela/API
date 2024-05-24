from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .api.serializers import TokenObtainSerilizer, TokenResponseSerilizer

@extend_schema(
        description='Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.',
        summary='User',
        responses={
                    200: {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'access': {'type': 'string', 'example': 'John'},
                                'refresh': {'type': 'string', 'example': 'Doe'},
                                'user_email': {'type': 'string', 'example': 'user@example.com'},
                                        },
                                },
                        },
                    },
        )
class Login(TokenObtainPairView):
    serializer_class = TokenObtainSerilizer
        
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.filter(email=request.user).first()
        
        if user:
            RefreshToken.for_user(user)
            request.user = None
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        return Response({"error": "Failed to logout."}, status=status.HTTP_400_BAD_REQUEST)