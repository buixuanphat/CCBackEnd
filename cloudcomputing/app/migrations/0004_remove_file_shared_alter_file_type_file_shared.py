# Generated by Django 5.1.7 on 2025-03-25 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_file_size_user_maximum_capacity_user_used_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='shared',
        ),
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='file',
            name='shared',
            field=models.ManyToManyField(related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]
