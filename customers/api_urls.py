from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.CustomerListAPIView.as_view(), name='list_api'),
	url(r'^create/', views.CustomerCreateAPIView.as_view(), name='create_api'),
	url(r'^(?P<pk>\d+)/$', views.CustomerDetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.CustomerUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', views.CustomerDeleteView.as_view(), name='delete'),
]