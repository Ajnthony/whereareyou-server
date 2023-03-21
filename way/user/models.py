import random
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required'))
    
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_moderator', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser: True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff: True')
        
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    genders = ['women','men']
    gender = random.choice(genders)
    random_number = random.choice(range(1, 100))
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('Email address'), unique=True)
    profile_url = models.ImageField(default=f'https://randomuser.me/api/portraits/{gender}/{random_number}.jpg', null=True)
    bio = models.TextField(max_length=200)
    address_line_1 = models.TextField(max_length=50)
    address_line_2 = models.TimeField(max_length=20, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    country = models.TextField(max_length=20)
    zip_code = models.CharField(max_length=5)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True) # email validation later?
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'