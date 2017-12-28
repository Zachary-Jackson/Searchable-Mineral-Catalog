from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'random', views.random_mineral, name='random_mineral'),
    url(r'search/group/(?P<pk>[\w\-]+)/$',
        views.search_group_selected, name='search_group_selected'),
    url(r'search/group', views.search_group, name='search_group'),
    url(r'search', views.search, name='search'),
]
