# Generated by Django 4.0.6 on 2022-09-28 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0003_alter_photoblog_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhotoBlog',
            new_name='Photos',
        ),
    ]