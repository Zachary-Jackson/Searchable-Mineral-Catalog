import random

from django.shortcuts import get_object_or_404, render

from .models import Mineral

# MINERAL_GROUPS currently unimplemented.
MINERAL_GROUPS = {'Arsenates', 'Borates', 'Carbonates', 'Halides',
                  'Native_Elements', 'Organic_Minerals', 'Oxides', 'Silicates',
                  'Sulfates', 'Sulfides', 'Sulfosalts', 'Phosphates' 'Other'}


def home(request):
    '''This is the homepage for the minerals app.'''
    mineral = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': mineral})


def detail(request, pk):
    '''This is the detail page for the minerals app.'''
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral':
                                                            mineral})


def random_mineral(request):
    '''This returns a random detail page for a mineral in the database.'''
    all_minerals = Mineral.objects.all()
    mineral = random.choice(all_minerals)
    return render(request, 'minerals/mineral_detail.html', {'mineral':
                                                            mineral})


def search(request):
    '''This takes the user to the advanced search page.'''
    return render(request, 'minerals/search.html')


def search_group(request):
    '''This takes the user to the search group page.'''
    return render(request,
                  'minerals/search_group.html')


def search_group_selected(request, pk):
    '''This returns the search results for a group the user searched.'''
    mineral = Mineral.objects.all().filter(group__icontains=pk)
    content_title = ("You are searching by " + pk.title() + ".")
    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': mineral, 'content_title': content_title})
