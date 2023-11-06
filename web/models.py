from django.db import models

# Create your models here.

class Portfolio (models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField()
    