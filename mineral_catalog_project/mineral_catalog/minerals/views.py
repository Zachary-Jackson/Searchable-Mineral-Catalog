import random

from django.shortcuts import get_object_or_404, render

from .models import Mineral


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
