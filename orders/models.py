from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Order(models.Model):
# 	store_id or store_id_alias	string	(Required) The id (or, optionally, id_alias) of the store the package will be picked up from
# order_reference	string	(Required) A reference to your internal order number
# customer	customer	(Required) A full customer
# ready_by	timestamp	(Required) A timestamp for when the packages will be ready
# packages	array	(Required) An array of one or more packages to be delivered
# delivery_window_id	string	(Required) The id of the chosen delivery window from your delivery estimate

	store_id = models.CharField(max_length=255)
	order_reference = models.CharField(max_length=255)
	customer = models.CharField(max_length=255)
	ready_by = models.CharField(max_length=255)
	packages = models.CharField(max_length=255)
	