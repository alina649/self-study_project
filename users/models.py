from django.contrib.auth.models import AbstractUser
from django.db import models

from platform_student.models import NULLABLE


# Create your models here.


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

