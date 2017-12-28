from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'random', views.random_mineral, name='random_mineral'),
]
