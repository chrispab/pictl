from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sample_list, name='sample_list'),
]
