from django.db import models

# Create your models here.

# class Portfolio (models.Model):
#     title=models.CharField(max_length=20)
#     image=models.ImageField()
#     description=models.TextField()
#     client=models.CharField(max_length=10)
#     industry=models.CharField(max_length=10)
#     service=models.CharField(max_length=30)
#     link=models.CharField(max_length=50)

#     def __str__(self):
#       return (self.title)

class Contact(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True,auto_now_add=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)