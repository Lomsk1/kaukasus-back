# Generated by Django 4.0.6 on 2022-08-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoblog',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]