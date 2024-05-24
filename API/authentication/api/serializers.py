from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, required=False, allow_null=True)
    last_name = serializers.CharField(max_length=50, required=False, allow_null=True)
    username = serializers.CharField(max_length=50, required=False, allow_null=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, min_length=8,)
    image = serializers.ImageField(required=False, allow_null=True)
    
    def validate_password(self, raw_password):
        return make_password(raw_password)
        
    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Este mail esta en uso")
        return value
        
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'image')

class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, required=False, allow_null=True)
    last_name = serializers.CharField(max_length=50, required=False, allow_null=True)
    username = serializers.CharField(max_length=50, required=False, allow_null=True)
    email = serializers.EmailField(required=True)
    image = serializers.ImageField(required=False, allow_null=True)
    
    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            if self.instance.email != value: 
                raise serializers.ValidationError("Este mail esta en uso")
        return value
        
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'image')
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(required=True, write_only=True, min_length=8,)
    new_password = serializers.CharField(required=True, write_only=True, min_length=8,)
    confirm_password  = serializers.CharField(required=True, write_only=True, min_length=8,)
                                    
    def validate_password(self, value):
        user = self.context.get('user')
        if not authenticate(username=user, password=value):
            raise serializers.ValidationError('La contraseña anterior es incorrecta')
        return value
    
    def validate(self, data):
        if data['new_password'] == data['confirm_password']:
            return data
        raise serializers.ValidationError('Las contraseñas nuevas no coinciden.')
    
    class Meta:
        model = get_user_model()
        fields = ('password', 'new_password', 'confirm_password')
        
class TokenObtainSerilizer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user':self.user.email,})
        return data

class TokenResponseSerilizer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    messagge = serializers.CharField()
    user_email = serializers.EmailField()