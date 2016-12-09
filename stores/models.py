from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	suite_number = models.CharField(max_length=255)
	address_line_1 = models.IntegerField()
	address_line_2 = models.EmailField(max_length=255, blank=True, default="")
	address_city = models.CharField(max_length=255)
	address_state = models.CharField(max_length=255)
	address_zipcode = models.IntegerField()