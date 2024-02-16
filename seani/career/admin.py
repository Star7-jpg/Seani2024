from django.contrib import admin
from .models import Career

# Register your models here.

class CareerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    list_filter = ['level']

admin.site.register(Career, CareerAdmin)