from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CustomerListCreateAPIView.as_view(), name='customer_list_api'),
	url(r'^(?P<pk>\d+)/$', views.CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer_detail_api'),
	url(r'^(?P<customer_pk>\d+)/packages/$', views.PackageListCreateAPIView.as_view(), name='package_list_api'),
	url(r'^(?P<customer_pk>\d+)/packages/(?P<pk>\d+)/$', views.PackageRetrieveUpdateDestroyAPIView.as_view(), name='package_detail_api'),

]