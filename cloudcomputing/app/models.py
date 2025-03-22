from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    maximum_capacity = models.FloatField(default=1024)
    used_capacity = models.FloatField(default=0)

    def __str__(self):
        return self.username

class File(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    size = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    shared = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared', null=True)

    def __str__(self):
        return self.name
