from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    place=models.CharField(max_length=30)
    def __str__(self):
        return self.username