from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^workers/$', views.workers, name='workers'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact_success/$', views.contact_success, name='contact_success'),
]