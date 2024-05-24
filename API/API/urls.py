
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.api.viewset import SignUpView, ProfileView, ChangePasswordView
from authentication.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/singup/', SignUpView.as_view(), name='signup'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/login/', Login.as_view() ,name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('api/logout/', Logout.as_view() ,name='logout'),
    path('api/perfil/', ProfileView.as_view() ,name='perfil'),
    path('api/change-password/', ChangePasswordView.as_view() ,name='change_password'),
]
