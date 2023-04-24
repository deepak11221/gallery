from django.contrib import admin
from .models import category
from .models import snippet
# Register your models here.

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    '''Admin View for category'''

    list_display = ('name', 'logo', 'description', 'created_on', 'updated_on')

@admin.register(snippet)
class snippetAdmin(admin.ModelAdmin):
    '''Admin View for snippet'''

    list_display = ('category', 'code', 'thumbnail', 'votes', 'description', 'created_on', 'updated_on')