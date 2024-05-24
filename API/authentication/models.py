from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from abstracts.models import AbstractModels
from .managers import CustomUserManager

def path_to_image(instance, filename):
    return f'perfil/{instance.id}/{filename}'

class CustomUser(AbstractBaseUser, AbstractModels):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to=path_to_image, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def has_module_perms(self, app_label):
        return True  # Cambia esto según tus reglas de permisos

    def has_perm(self, perm, obj=None):
        
        return True  # Cambia esto según tus reglas de permisos
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"