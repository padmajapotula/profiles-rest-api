from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Managet for User Profiles """
    def crete_user(self,email,name,password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return users

    def create_supersuser(self,email,name,password):
        """ Crete and save a new superuser with given details """
        user = self.create_user(email,name,password)

        user.is_superuser =True
        user.is_staff = True
        user.save(using=self.db)

        return user

class Userprofile(AbstractBaseUser,PermissionsMixin):
    """ Database Models for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS=["name"]

    def get_full_name(self):
        """retrive full name of user """
        return self.name

    def get_sort_name(self):
        """"retrive short name """
        return self.name

    def __str__(self):
        """ return string representation of the user """
        return self.email
