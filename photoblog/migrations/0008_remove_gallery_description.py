# Generated by Django 4.0.6 on 2022-09-29 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0007_gallery_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
    ]
