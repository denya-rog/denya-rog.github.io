from django import forms
from .models import *

class subscriberForm(forms.ModelForm):
    class Meta:
        
        model = Subscriber
#        fields=['']  #  filds include can be passed
        exclude = [""]     #filds exclude


class subscriberName(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields=['name']  #  filds include can be passed
        exclude = [""]  # filds exclude