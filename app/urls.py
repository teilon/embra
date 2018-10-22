from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^2/$', views.index2, name='index2'),
    url(r'^3/$', views.index3, name='index3'),
    url(r'^storage/$', views.storage, name='storage'),
    url(r'^start_storage/$', views.start_storage, name='start_storage'),

    url(r'^clients/$', views.client_list, name='client_list'),
    url(r'^client/(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),

    url(r'^temp/$', views.temp, name='temp'),

    url(r'^transactions/$', views.transaction_list, name='transaction_list'),
    url(r'^transaction/new/$', views.transaction_new, name='transaction_new'),
]
