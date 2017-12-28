from django.shortcuts import render


def home(request):
    '''This is the homepage for the minerals app.'''
    return render(request, 'layout.html')
