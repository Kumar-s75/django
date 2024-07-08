from django import forms
from .models import ChaiVarity

class  ChaiVarityForm(forms.Form)
    chai_varity=forms.CharField()