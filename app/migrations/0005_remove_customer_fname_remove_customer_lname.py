# Generated by Django 5.0.3 on 2024-04-05 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_user_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
    ]
