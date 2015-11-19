from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class SomeUser(AbstractBaseUser):
    '''
    Custom User class
    '''

    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False) #Default to False in order to activate via email
    is_admin = models.BooleanField(default=False) #Default to False in order to prevent users from being admin when they register

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
