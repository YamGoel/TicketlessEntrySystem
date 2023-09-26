from django.db import models

# Create your models here.

class Users(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Unique(models.Model):
    uid=models.CharField(max_length=6)

    def __str__(self):
        return self.uid