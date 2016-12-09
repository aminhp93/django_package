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
from rest_framework import permissions

from . import serializers
from builtins import (super)
from . import models


# ==============================================================================
# 							Driver View
# ==============================================================================


class DriverCreateView(generic.CreateView):
	fields = ("name", "photo_url", "longitude", "latitude", "email", "address_line_1", "address_line_2", "address_city", "address_state", "address_zipcode")
	model = models.Driver

class DriverListView(generic.ListView):
	model = models.Driver
	context_object_name = 'drivers'

class DriverDetailView(generic.DetailView):
	model = models.Driver

class DriverUpdateView(generic.UpdateView):
	fields = ("name", "photo_url", "longitude", "latitude", "email", "address_line_1", "address_line_2", "address_city", "address_state", "address_zipcode")
	model = models.Driver

class DriverDeleteView( generic.DeleteView):
	model = models.Driver
	success_url = reverse_lazy('drivers:list')


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
	permission_classes = (permissions.DjangoModelPermissions,)


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















	


