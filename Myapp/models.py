# Create your models here.
#author raniniveda
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    mobile_number = models.CharField(blank=True, max_length=10)
