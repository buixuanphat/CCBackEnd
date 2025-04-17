from datetime import datetime, date, timezone, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


from rest_framework.exceptions import ValidationError


from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    maximum_capacity = models.FloatField(default=1024 * 1024 * 1024)  # 1GB
    used_capacity = models.FloatField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def check_valid(self):
        if self.used_capacity > self.maximum_capacity:
            raise ValidationError('Bạn đã sử dụng hết dung lượng.')

    def upgrade_plan(self):
        now = timezone.now()
        if self.expiration_date and self.expiration_date > now:
            raise ValidationError('Gói hiện tại vẫn còn hiệu lực. Không thể đăng ký gói mới.')

        self.maximum_capacity = 2 * 1024 * 1024 * 1024  # 2GB
        self.expiration_date = now + timedelta(days=30)
        self.save()

    def check_expiration(self):
        now = timezone.now()
        if self.expiration_date and self.expiration_date < now and self.maximum_capacity > 1024 * 1024 * 1024:
            self.maximum_capacity = 1024 * 1024 * 1024  # Reset về 1GB
            self.save()

    def __str__(self):
        return self.username





class File(models.Model):
    name = models.TextField()
    type = models.TextField()
    link = models.TextField()
    size = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')


    def __str__(self):
        return self.name

class FileShare(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    shared_date = models.DateTimeField(auto_now_add=True)




