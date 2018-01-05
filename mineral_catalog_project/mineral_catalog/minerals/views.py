import collections
import string
import random

from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Mineral


def home(request):
    '''This is the homepage for the minerals app.'''
    mineral = Mineral.objects.all()
    content_title = ("Here are all " + str(len(mineral)) +
                     " minerals in the database")
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': mineral, 'content_title': content_title})


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


def search_help(request):
    '''This takes the user to the search help page.'''
    return render(request, 'minerals/help.html')


def search_color(request):
    '''This takes the user to the search by color page.'''
    # This is a list of collors guarenteed to get results.
    colors = ['amber', 'amethyst', 'apple', 'azure', 'black', 'blue', 'blood',
              'bluish', 'brass', 'bronze', 'brown', 'colorless', 'copper',
              'cream', 'crimson', 'cyan', 'dark', 'dark', 'dull', 'dull',
              'emerald', 'gold', 'gray', 'green', 'greenish', 'grey', 'indigo',
              'iridescent', 'lavender', 'lead', 'metallic', 'olive', 'orange',
              'peach', 'pale', 'pink', 'pistachio', 'purple', 'purplish',
              'red', 'rose', 'rosy', 'rosy', 'ruby', 'silver', 'steel',
              'steel', 'transparent', 'turquoise', 'violet', 'white', 'yellow']

    colors = collections.OrderedDict.fromkeys(colors)
    return render(request, 'minerals/search_color.html',
                  {'colors': colors})


def search_color_selected(request, pk=None):
    '''This takes the user to crystal system search page.'''
    minerals = Mineral.objects.all().filter(color__icontains=pk)
    content_title = (
        (str(len(minerals)) + " results for the color  "))
    content_end = pk
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'content_title': content_title,
                   'content_end': content_end})


def search_color_user(request):
    '''This returns the search results for a color the user entered.'''
    search = request.GET.get('search')
    # This searches for the user's color.
    minerals = Mineral.objects.all().filter(color__icontains=search)

    content_title = (
        (str(len(minerals)) + " results for the color "))
    content_end = search

    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title,
         'content_end': content_end})


def search_crystal_system(request):
    '''This takes the user to crystal system search page.'''
    content_title = 'Please select the crystal system you want'
    return render(request, 'minerals/search_crystal_system.html',
                  {'content_title': content_title})


def search_crystal_system_selected(request, pk):
    '''This takes the user to crystal system search page.'''
    minerals = Mineral.objects.all().filter(crystal_system__icontains=pk)
    content_title = (
        (str(len(minerals)) + " results for the crystal system  "))
    content_end = (pk.title())
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'content_title': content_title,
                   'content_end': content_end})


def search_letter(request):
    '''This takes the user to the search letter page.'''
    # This creates an OrderedDict for each of the uppercase letters.
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

    content_title = (
        (str(len(minerals)) + " results for the letter  "))
    content_end = (pk.title())

    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title,
         'content_end': content_end})


def search_group(request):
    '''This takes the user to the search group page.'''
    return render(request,
                  'minerals/search_group.html')


def search_group_selected(request, pk):
    '''This returns the search results for a group the user searched.'''
    minerals = Mineral.objects.all().filter(group__icontains=pk)

    # This checks to see if the user is searching by Native Elements or
    # Organic Minerals and changes the pk name if so.
    if pk.lower() == 'organic':
        pk = 'Organic Minerals'
    elif pk.lower() == 'native':
        pk = 'Native Elements'

    content_title = (
        (str(len(minerals)) + " results for the group "))
    content_end = (pk.title())

    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title,
         'content_end': content_end})


def search_term_selected(request):
    '''This returns the search results for a term the user searched.'''
    search = request.GET.get('search')
    # This searches every characteristic a mineral can have.
    minerals = Mineral.objects.all().filter(
        Q(name__icontains=search) | Q(image_caption__icontains=search) |
        Q(category__icontains=search) | Q(formula__icontains=search) |
        Q(strunz_classification__icontains=search) |
        Q(color__icontains=search) | Q(crystal_system__icontains=search) |
        Q(cleavage__icontains=search) |
        Q(mohs_scale_hardness__icontains=search) |
        Q(luster__icontains=search) | Q(streak__icontains=search) |
        Q(diaphaneity__icontains=search) |
        Q(optical_properties__icontains=search) |
        Q(refractive_index__icontains=search) |
        Q(crystal_habit__icontains=search) |
        Q(specific_gravity__icontains=search) | Q(group__icontains=search))

    content_title = (
        (str(len(minerals)) + " results for the search term "))
    content_end = search

    return render(
        request, 'minerals/mineral_list.html',
        {'minerals': minerals, 'content_title': content_title,
         'content_end': content_end})
