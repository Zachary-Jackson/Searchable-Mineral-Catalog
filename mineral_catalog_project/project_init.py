import json
import os
import sys

from django.core.wsgi import get_wsgi_application

# Much of this file was written by chrisrh. chrisrh helped me with
# some unicode errors that this file fixed. I modified some
# of the information to fit my specific program.

# Uses this script file, to find the directory we are currently in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# First we need the path to the project
# This can be hardcoded, but to be OS capatible
# The 'os' module is what we need
project_path = os.path.join(BASE_DIR)

# This environ variable is so Django module itself can find all our project
# stuff.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MYPROJECT.settings")
# notice I changed MYPROJECT to the package that has the settings.py file.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# We want to append our project path to the system so Django can find it.
sys.path.append(project_path)

# This is so my local_settings.py gets loaded.
# os.chdir(proj_path)

# This will ensure our project models get loaded.
application = get_wsgi_application()

# This import is required down here otherwise the file will not work.
from mineral_catalog.minerals.models import Mineral

current_location = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(current_location,
                             'mineral_catalog/minerals/fixtures/minerals.json')


def minerals_dictionary():
    with open(file_location, encoding="utf-8") as jsonfile:
        minerals = json.load(jsonfile)
        return minerals


def key_checker(item, key_name):
    '''This checks to see if each key exsists and if so returns the contents.
       Otherwise returns an empty string.'''
    try:
        returned_contents = item[key_name]
    except KeyError:
        return ''
    else:
        return returned_contents


def populate_database():
    '''This populates the database for each mineral in the json file.'''
    # I can use my app models now...
    mineral_json = minerals_dictionary()
    for item in mineral_json:
        alpha = Mineral()
        alpha.name = key_checker(item, 'name')
        alpha.image_filename = key_checker(item, 'image filename')
        alpha.image_caption = key_checker(item, 'image caption')
        alpha.category = key_checker(item, 'category')
        alpha.formula = key_checker(item, 'formula')
        alpha.strunz_classification = key_checker(item,
                                                  'strunz classification')
        alpha.color = key_checker(item, 'color')
        alpha.crystal_system = key_checker(item, 'crystal system')
        alpha.cleavage = key_checker(item, 'cleavage')
        alpha.mohs_scale_hardness = key_checker(item, 'mohs scale hardness')
        alpha.luster = key_checker(item, 'luster')
        alpha.streak = key_checker(item, 'streak')
        alpha.diaphaneity = key_checker(item, 'diaphaneity')
        alpha.optical_properties = key_checker(item, 'optical properties')
        alpha.refractive_index = key_checker(item, 'refractive index')
        alpha.crystal_habit = key_checker(item, 'crystal habit')
        alpha.specific_gravity = key_checker(item, 'specific gravity')
        alpha.group = key_checker(item, 'group')
        alpha.save()


if __name__ == '__main__':
    populate_database() # run our script and we can use our django apps now.
