from django import forms
from .models import graph

class graphForm(forms.ModelForm):
    class Meta:
        model = graph
        fields = ('name','logo','description','category','created_on','updated_on',)