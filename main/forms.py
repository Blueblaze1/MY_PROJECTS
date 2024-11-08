from django import forms
from .models import *

class txtform(forms.ModelForm):
    class Meta:
        model = Txt
        fields = ['text_file']
    
