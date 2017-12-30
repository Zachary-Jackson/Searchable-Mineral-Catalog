from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'random', views.random_mineral, name='random_mineral'),
    url(r'search/color/user',
        views.search_color_user, name='search_color_user'),
    url(r'search/color/(?P<pk>[\w\-]+)/$',
        views.search_color_selected, name='search_color_selected'),
    url(r'search/color', views.search_color, name='search_color'),
    url(r'search/crystalsystem/(?P<pk>[\w\-]+)/$',
        views.search_crystal_system_selected,
        name='search_crystal_system_selected'),
    url(r'search/crystalsystem',
        views.search_crystal_system, name='search_crystal_system'),
    url(r'search/letter/(?P<pk>[\w\-]+)/$',
        views.search_letter_selected, name='search_letter_selected'),
    url(r'search/letter', views.search_letter, name='search_letter'),
    url(r'search/group/(?P<pk>[\w\-]+)/$',
        views.search_group_selected, name='search_group_selected'),
    url(r'search/group', views.search_group, name='search_group'),
    url(r'search/term/',
        views.search_term_selected, name='search_term_selected'),
    url(r'search/help/', views.search_help, name='search_help'),
    url(r'search', views.search, name='search'),
]
