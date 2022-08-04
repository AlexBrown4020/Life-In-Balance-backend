import datetime
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.id_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username= models.CharField(
        max_length=30,
        unique=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.username

    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin