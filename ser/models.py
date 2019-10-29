from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
class Post(models.Model):

    aut = models.CharField(max_length=255 )
    flat_number = models.CharField(max_length=30)  

   
    time = models.CharField(max_length=255 )

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.aut


class Item(models.Model):
    aut = models.CharField(max_length=255 )
   
    bread = models.IntegerField(validators=[MinValueValidator(0)])
    water =  models.IntegerField(validators=[MinValueValidator(0)])
    milk =  models.IntegerField(validators=[MinValueValidator(0)])
    rice =  models.IntegerField(validators=[MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True,null=True)
    flat_number = models.CharField(max_length=30)                       #######new for admin login
    def __str__(self):
        return self.aut
    def get_total(self):
        total = 0
        total = total+self.bread*35
        total = total+self.water*50
        total = total+self.milk*22
        total = total+self.rice*40
        return total


