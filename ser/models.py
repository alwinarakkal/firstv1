from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):

    aut = models.CharField(max_length=255 )


    # flat_number = models.CharField(max_length=255 )   #neww2222
    time = models.CharField(max_length=255 )

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
    def get_total(self):
        total = 0
        total = total+self.bread*35
        total = total+self.water*50
        total = total+self.milk*22
        total = total+self.rice*40
        return total


