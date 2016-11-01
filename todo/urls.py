from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^index/(?P<page>\d*)$', views.index,name='index'),
    url(r'^add/$',views.add,name='add'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
    url(r'^edit/(?P<id>\d+)/$',views.edit,name='edit'),
    url(r'^status/(?P<id>\d+)$',views.status,name='status'),
]