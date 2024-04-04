from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):

    
    User_type =[
        ('none','Select Type'),
        ('Rider','Rider'),
        ('Admin','Admin')
    ]

# IN this list of tupple the first one is value and second one is Label
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    nid = models.CharField(max_length=20)
    # user_type = models.CharField(max_length=10, choices=[('none','Select Type'),('Rider', 'rider'),('Admin', 'admin')])
    # Alternative way to do this
    user_type = models.CharField(max_length=10, choices=User_type, default="none")

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )

    email = models.EmailField(unique=True)  # Define email as a unique field

    # Remove 'email' from REQUIRED_FIELDS since it's already set as USERNAME_FIELD
    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'  # Set the email as the unique identifier for authentication

    def __str__(self):
        return self.username


