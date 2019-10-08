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
    c1 = (
        ('a', '1 packet'),('f', '2 packet'),('g', '3 packet'),
    
   
    )
        
    c2 = (
        ('b', '1 CAN'),('h', '2 CAN'),('i', '3 CAN'),
    
   
    )    
    c3 = (
        ('c', '1 packet'),('d', '2 packet'),('e', '3 packet'),
    
   
    )
    c4 = (
        ('j', '1 kg'),('k', '3 kg'),('l', '5 kg'),('z', '10 kg'),
    
   
    )
    aut = models.CharField(max_length=255 )
    bread = models.CharField(max_length=1, choices=c1,blank=True)
    water = models.CharField(max_length=1, choices=c2,blank=True)
    milk = models.CharField(max_length=1, choices=c3,blank=True)
    rice = models.CharField(max_length=1, choices=c4,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.aut


