from django.db import models

class Guide(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')
    dis=models.TextField()

class Place(models.Model):
    name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='pics')
    dis=models.TextField()

def __str__(self):
    return self.name

