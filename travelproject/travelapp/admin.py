from django.contrib import admin

from . models import Guide
from . models import Place

# Register your models here.

admin.site.register(Guide)
admin.site.register(Place)
