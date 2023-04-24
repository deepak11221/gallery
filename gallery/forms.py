from django import forms
from .models import category
from .models import snippet

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ('name','logo','description',)

class snippetForm(forms.ModelForm):
    class Meta:
        model = snippet
        fields = ('category','code','thumbnail','votes','description',)