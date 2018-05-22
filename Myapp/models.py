# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete= models.CASCADE)
    address = models.TextField(default='',blank=True)	
    pincode = models.CharField(max_length=6,blank=True)
    mobile = models.CharField(max_length=10,blank=True)
    birth_date = models.DateField()


