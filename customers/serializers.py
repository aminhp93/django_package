from . import models
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', "first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode")
		model = models.Customer

class PackageSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', "name", "price", "SKU", "height", "width", "depth", "weight", "customer")
		model = models.Package
