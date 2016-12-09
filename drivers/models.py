from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Driver(models.Model):
	name	string	
photo_url	string	A URL of the driver’s profile photo
longitude	float	The longitude of the driver’s current location
latitude	float	The latitude of the driver’s current location
delivery_photo_url	string	A URL for the proof of delivery photo taken at dropoff if present
destination_signature	hash	A hash containing photo_url and last_name if present
photo_url	string	A URL of the signature
last_name	string	The last name of the person who signed for the package
	
	name = models.CharField(max_length=255)
	photo_url = models.URLField(unique=True)
	longitude = models.CharField(max_length=255)
	latitude = models.IntegerField()
	email = models.EmailField()
	address_line_1 = models.CharField(max_length=255)
	address_line_2 = models.TextField(blank=True, default='')
	address_city = models.CharField(max_length=255)
	address_state = models.CharField(max_length=255)
	address_zipcode = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

