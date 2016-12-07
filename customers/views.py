from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from builtins import (super)
from . import models

class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
	fields = ("first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode")
	model = models.Customer

class CustomerListView(generic.ListView):
	model = models.Customer
	context_object_name = 'customers'

class CustomerDetailView(generic.DetailView):
	model = models.Customer

class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
	fields = ("first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode")
	model = models.Customer

class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
	model = models.Customer
	success_url = reverse_lazy('customers:list')


class CustomerListAPIView(APIView):

	def get(self, request, format=None):
		customers = models.Customer.objects.all()
		serializer = serializers.CustomerSerializer(customers, many=True)
		return Response(serializer.data)

# class CustomerDetailAPIView(APIView):
	















	


