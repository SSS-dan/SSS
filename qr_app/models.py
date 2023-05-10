from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator


class NewUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username',]

class NewUserAccountManager(BaseUserManager):

    def create_superuser(self,username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
      
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
       
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        user =  self.create_user(username, password, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username,password,**other_fields):
        if not email:
            raise ValueError('Email address is required!')
        email = self.normalize_email(email)
        if password is not None:
            user = self.model(username=username,password=password, **other_fields)
            user.save()
        else:
            user = self.model(username=username, password=password,**other_fields)
            user.set_unusable_password()
            user.save()

        return user