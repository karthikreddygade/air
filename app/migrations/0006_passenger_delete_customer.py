# Generated by Django 5.0.3 on 2024-04-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_customer_fname_remove_customer_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pswd', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
