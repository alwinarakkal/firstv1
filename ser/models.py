from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):

    aut = models.CharField(max_length=255 )


    flat_number = models.CharField(max_length=255 )   #neww2222

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.aut


class Item(models.Model):
    aut = models.CharField(max_length=255 )
   
    bread = models.IntegerField()
    water =  models.IntegerField()
    milk =  models.IntegerField()
    rice =  models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.aut


