# Generated by Django 4.0.6 on 2022-09-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_alter_services_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
