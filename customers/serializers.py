from . import models
from rest_framework import serializers



class PackageSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', "name", "price", "SKU", "height", "width", "depth", "weight", "customer")
		model = models.Package

class CustomerSerializer(serializers.ModelSerializer):
	# packages = PackageSerializer(many=True, read_only=True)
	# packages = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api_v2:package-detail')
	packages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		fields = ('id', "first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode", 'packages')
		model = models.Customer