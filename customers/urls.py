from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.DriverListView.as_view(), name='list'),
	url(r'^create/', views.DriverCreateView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', views.DriverDetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.DriverUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', views.DriverDeleteView.as_view(), name='delete'),
]