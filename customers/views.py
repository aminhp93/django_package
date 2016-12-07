from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from builtins import (super)
from . import models

class CustomerCreateView(generic.CreateView):
	fields = ("first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode")
	model = models.Customer

class CustomerListView(generic.ListView):
	model = models.Customer
	context_object_name = 'customers'

class CustomerDetailView(generic.DetailView, generic.UpdateView):
	fields = ("first_name", "last_name")
	model = models.Customer

class CustomerUpdateView(generic.UpdateView):
	fields = ("first_name", "last_name", "business_name", "phone", "email", "address_line_1", "address_city", "address_state", "address_zipcode")
	model = models.Customer

class CustomerDeleteView(generic.DeleteView):
	model = models.Customer
	success_url = reverse_lazy('customers:list')



	


