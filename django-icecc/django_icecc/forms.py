# -*- coding: utf-8 -*-
from django import forms

class BlockForm(forms.Form):
    """
    A simple form that takes the name of a CS host for removal
    """
    host = forms.CharField(label='', widget=forms.Textarea)




