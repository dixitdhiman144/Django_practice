from django.db import models

# Create your models here.

class Destination(models.Model):
    # id : models.IntegerField() removing id because in in <python make makemigrations> cmnd it will automaticaly created
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=1000, default='Good City')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)