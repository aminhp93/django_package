from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import detail_route
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

# ==============================================================================
# 							APIView
# ==============================================================================

class CustomerListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Customer.objects.all()
	serializer_class = serializers.CustomerSerializer
	
class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Customer.objects.all()
	serializer_class = serializers.CustomerSerializer

class PackageListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Package.objects.all()
	serializer_class = serializers.PackageSerializer

	def get_queryset(self):
		return self.queryset.filter(customer_id=self.kwargs.get('customer_pk'))

	def perform_create(self, serializer):
		customer = get_object_or_404(models.Customer, pk = self.kwargs.get('customer_pk'))
		serializer.save(customer = customer)
	
class PackageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Package.objects.all()
	serializer_class = serializers.PackageSerializer

	def get_object(self):
		return get_object_or_404(self.get_queryset(), customer_id = self.kwargs.get('customer_pk'), pk=self.kwargs.get('pk'))

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = models.Customer.objects.all()
	serializer_class = serializers.CustomerSerializer

	@detail_route(methods=['get'])
	def packages(self, request, pk=None):
		self.pagination_class.page_size = 1
		packages = models.Package.objects.filter(customer_id=pk)

		page = self.paginate_queryset(packages)
		if page is not None:
			serializer = serializers.PackageSerializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		# customer = self.get_object()
		
		serializer = serializers.PackageSerializer(packages, many=True)
		return Response(serializer.data)

class PackageViewSet(mixins.CreateModelMixin,
					mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					viewsets.GenericViewSet):
	queryset = models.Package.objects.all()
	serializer_class = serializers.PackageSerializer















	


