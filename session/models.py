from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
	#profile_pic=models.ImageField(upload_to='profile_pics/',blank=True)
	sex=models.CharField(max_length=10,null=True)
	age=models.IntegerField(null=True)
	phone=models.IntegerField(null=True)
	address=models.CharField(max_length=200,null=True,blank=True)
	stars=models.IntegerField(null=True)
	following = models.ManyToManyField("self", symmetrical = False, related_name = "followers")
class User(models.Model):
	first_name=models.CharField(max_length=50)

