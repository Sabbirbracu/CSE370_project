from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    nid = models.CharField(max_length=20)
    user_type = models.CharField(max_length=10, choices=[('none','none'),('rider', 'aider'),('admin', 'admin')])

    # Add unique related_name arguments for groups and user_permissions
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

    def __str__(self):
        return self.username
