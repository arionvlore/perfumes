
# Create your models here.
from __future__ import unicode_literals
from django.db import models


class Employer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "employer"


class Subscribe(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "subscribe"


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Pay(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    payment = models.CharField(max_length=10)

    class Meta:
        db_table = "Pay"

class Paypal(models.Model):
            first_name = models.CharField(max_length=20)
            last_name = models.CharField(max_length=30)
            payment = models.CharField(max_length=10)

            class Meta:
                db_table = "Paypal"


