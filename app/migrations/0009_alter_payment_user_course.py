# Generated by Django 3.2.5 on 2021-08-02 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210802_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usercourse'),
        ),
    ]
