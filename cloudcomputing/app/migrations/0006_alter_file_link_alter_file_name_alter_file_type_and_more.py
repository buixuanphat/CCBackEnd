# Generated by Django 5.1.7 on 2025-03-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_file_shared_fileshare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='maximum_capacity',
            field=models.FloatField(default=1073741824),
        ),
    ]
