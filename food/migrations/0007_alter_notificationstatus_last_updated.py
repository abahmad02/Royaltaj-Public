# Generated by Django 4.2.6 on 2023-12-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_notificationstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationstatus',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
