from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    '''Admin View for profile'''

    list_display = ('name', 'email', 'phone', 'address', 'city', 'state', 'pincode', 'created_on', 'updated_on')