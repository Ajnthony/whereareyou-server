""" User manager and model """
import random
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """ User manager """
    
    def create_user(self, email, password=None, **extra_fields):
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
    """ User model """
    
    # basic info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('Email address'), unique=True)
    profile_url = models.ImageField(default='', null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    # address
    address_line_1 = models.TextField(max_length=50)
    address_line_2 = models.TextField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    country = models.TextField(max_length=20)
    zip_code = models.CharField(max_length=5)
    
    # dates
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(default=None, null=True, blank=True)
    
    
    # permissions
    is_active = models.BooleanField(default=True) # email validation later?
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return self.display_name if self.display_name else full_name
    
    def save(self, *args, **kwargs):
        created = not self.pk
        
        if created and not self.profile_url:
            genders = ['women','men']
            gender = random.choice(genders)
            random_number = random.choice(range(1, 100))
            self.profile_url = f'https://randomuser.me/api/portraits/{gender}/{random_number}.jpg'
            
        return super().save(*args, **kwargs)
    