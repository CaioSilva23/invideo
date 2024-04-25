from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    
    def _create_user(self, email: str, password: str, **extra_fields: Any) -> Any:
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
    

class Users(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(null=True, blank=True, max_length=150)
   
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    
    objects = UserManager()

    def __str__(self):
        return self.email
