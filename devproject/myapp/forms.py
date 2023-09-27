from django import forms
from myapp.models import datas

class datasforms(forms.ModelForm):
    class Meta:
        model = datas
        fields = ['titile', 'day_travel', 'budget', 'detail']
        widgets = {
            'titile': forms.TextInput(attrs={'class': 'form-control'}),
            'day_travel': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'})
        }
