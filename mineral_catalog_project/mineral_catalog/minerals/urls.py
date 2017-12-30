from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'random', views.random_mineral, name='random_mineral'),
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

# unimplemented url patterns
# url(r'search/mohsscale/(?P<num1>\d+)/(?P<num2>\d+)/$',
#     views.search_mohsscale_selected, name='search_mohsscale_selected'),
# url(r'search/mohsscale', views.search_mohsscale, name='search_mohsscale'),
