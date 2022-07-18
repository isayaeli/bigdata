from django.contrib import admin

from .models import Life_Expectancy
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Life_Expectancy)
admin.site.unregister(Group)

admin.site.site_header = 'Big Data Admin'