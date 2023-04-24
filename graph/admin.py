from django.contrib import admin
from .models import graph

# Register your models here.

@admin.register(graph) 
class graphAdmin(admin.ModelAdmin):
    '''Admin View for graph'''

    list_display = ('name', 'logo','description', 'category', 'created_on', 'updated_on')