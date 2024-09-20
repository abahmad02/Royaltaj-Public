# Generated by Django 4.2.6 on 2023-12-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.ImageField(upload_to='payments/')),
                ('date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.order')),
            ],
        ),
    ]
