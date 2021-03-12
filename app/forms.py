from django import forms
from .models import Linija, Stanica

class LinijaModelForm(forms.ModelForm):
    class Meta:
        model = Linija
        fields = ['naziv', 'stanice']

    naziv = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control mb-5'})))
    
    stanice = forms.ModelMultipleChoiceField(
    queryset=Stanica.objects.all(),
    widget=forms.CheckboxSelectMultiple(attrs={'onchange':'checkboxes()'
    })
)

class StanicaModelForm(forms.ModelForm):
    class Meta:
        model = Stanica
        fields = ['naziv', 'opis', 'tacka']

    naziv = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    opis = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    tacka = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
