# Generated by Django 5.1.7 on 2025-04-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_file_link_alter_file_name_alter_file_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
