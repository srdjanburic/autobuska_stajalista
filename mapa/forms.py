from django import forms
from app.models import Linija, Stanica

class DodajLinijuForm(forms.Form):
    naziv = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control mt-1 mb-1'})))
    stanice = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control mb-1', 'readonly':'true', 'style':'display:none'})))

