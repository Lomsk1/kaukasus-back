# Generated by Django 4.0.6 on 2022-09-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termsAndConditions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsandconditions',
            name='body',
            field=models.TextField(blank=True, default='terms and conditions'),
        ),
    ]