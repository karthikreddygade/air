from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pswd = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Tickets(models.Model):
    source = models.CharField(max_length=100)
    start_date = models.DateField()
    time = models.TimeField()
    destination = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.source



class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pswd = models.CharField(max_length=10)

    def __str__(self):
        return self.name

