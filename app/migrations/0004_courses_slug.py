# Generated by Django 3.2.5 on 2021-07-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
