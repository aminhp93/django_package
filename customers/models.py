from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Customer(models.Model):

	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	business_name = models.CharField(max_length=255)
	phone = models.IntegerField()
	email = models.EmailField(max_length=255)
	address_line_1 = models.CharField(max_length=255)
	address_city = models.CharField(max_length=255)
	address_state = models.CharField(max_length=255)
	address_zipcode = models.IntegerField()

	def __str__(self):
		return self.first_name

	def get_absolute_url(self):
		return reverse("customers:detail", kwargs={"pk": self.pk})

class Package(models.Model):

	name = models.CharField(max_length=255)
	price = models.IntegerField()
	SKU = models.CharField(max_length=255)
	height = models.IntegerField()
	width = models.IntegerField()
	depth = models.IntegerField()
	weight = models.IntegerField()
	customer = models.ForeignKey(Customer, related_name="packages")
	location = models.CharField(max_length=255)
