from django.db import models
# from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField(validators=[MinLengthValidator(8, 'the filed must contain at least 8 characters')])
    # is_authenticated = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        return str(self.username)