from django.contrib import admin
from .models import Cv, Section, SubSection, Content


array = [Cv, Section, SubSection, Content]
admin.site.register(array)