from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=24)
    description = models.CharField(max_length=1024)
    img_url = models.CharField(max_length=512)

    #this is to change the name of an item in admin dashboard
    def __str__(self):
        return self.name


