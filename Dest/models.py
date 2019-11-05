from django.db import models


# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100, null=True ,blank= True)
    desc = models.TextField(null=True ,blank= True)
    price = models.IntegerField(null=True ,blank= True)
    img = models.ImageField(upload_to='pics',blank= True,null=True)
    offer = models.BooleanField(default = False,blank=True,null = True )

class Booking(models.Model):
    firstname  = models.CharField(max_length=100,blank= True,null=True)
    lastname  = models.CharField(max_length=100,blank= True,null=True)
    email = models.EmailField(blank=True, unique=True)
    destination = models.TextField(null=True,blank= True)
    date = models.DateField(blank= True,null=True)
    hour = models.IntegerField(blank= True,null=True)
    minute = models.IntegerField(blank= True,null=True)

   