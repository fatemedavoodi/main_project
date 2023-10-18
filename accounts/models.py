from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager,PermissionsMixin



# class CustomeUser(AbstractUser):
#     id_code = models.CharField(max_length=10,null=True, blank=True)
#     mobile = models.CharField(max_length=20,null=True, blank=True)
#     image = models.ImageField(upload_to='users', default='user.jpg')

class CustomeBaseUserManager(BaseUserManager):
    def create_user(self, id_code, password, **extra_fields):
        if not id_code:
            raise ValueError('The given id_code must be set')
        if len(id_code) != 10 or id_code.isnumeric == False:
            raise ValueError('The given id_code is not true')
        user = self.model(id_code=id_code, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, id_code, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(id_code, password, **extra_fields)



class CustomeUser(AbstractBaseUser, PermissionsMixin):
    id_code = models.CharField(unique=True, max_length=10)
    username  = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'id_code'
    REQUIRED_FIELDS = []

    objects = CustomeBaseUserManager()

    def __str__(self):
        return self.id_code