from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'color']
        labels = {
            'brand': 'Marque',
            'model': 'Modèle',
            'year': 'Année',
            'color': 'Couleur',
        }
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=[(i, i) for i in range(2000, 2023)], attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['year'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
        })

        self.fields['color'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
        })

        self.fields['brand'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
            'data-search-enabled': 'true',
        })

        self.fields['color'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
            'data-search-enabled': 'true',
        })
