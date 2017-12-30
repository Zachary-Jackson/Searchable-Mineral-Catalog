from django.contrib import admin

from .models import Mineral

# This allows the admin to edit the Mineral model.
admin.site.register(Mineral)
