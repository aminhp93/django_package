from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class CustomerCreateAPIView(APIView):

	def get(self, request, format=None):
		customers = models.Customer.objects.all()
		serializer = serializers.CustomerSerializer(customers, many=True)
		return Response(serializer.data)
		
	def post(self, request, format=None):
		serializer = serializers.CustomerSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	















	


