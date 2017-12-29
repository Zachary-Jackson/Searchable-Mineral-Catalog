import collections
import string
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


def search_letter(request):
    '''This takes the user to the search letter page.'''
    letters = string.ascii_uppercase
    letters = collections.OrderedDict.fromkeys(letters)
    content_title = "Please select the first letter for the mineral you want."
    return render(request, 'minerals/search_letter.html',
                  {'letters': letters, 'content_title': content_title})


def search_letter_selected(request, pk):
    '''This returns the search results for a letter the user has chosen.'''
    mineral_list = Mineral.objects.all()
    minerals = []
    # This gets every mineral that matches the pk.
    for item in mineral_list:
        if item.name[0].upper() == pk.upper():
            minerals.append(item)
    content_title = ("You are searching by the letter " + pk.title() + ".")
    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title})


def search_group(request):
    '''This takes the user to the search group page.'''
    return render(request,
                  'minerals/search_group.html')


def search_group_selected(request, pk):
    '''This returns the search results for a group the user searched.'''
    minerals = Mineral.objects.all().filter(group__icontains=pk)
    content_title = ("You are searching by " + pk.title() + ".")
    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title})
