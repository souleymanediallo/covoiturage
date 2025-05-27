from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from .models import Homework, DAYS_OF_WEEK
from django.core.exceptions import ValidationError


def generate_time_choices(interval=30):
    times = []
    for hour in range(24):  # pour 0 à 23 heures
        for minute in range(0, 60, interval):  # intervalle de minutes
            times.append((f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}'))
    return times


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['start_city', 'end_city', 'price', 'seat_go', 'seat_return', 'description', 'role',
                  *[f"{code}_active" for code, _ in DAYS_OF_WEEK],
                  *[f"{code}_start" for code, _ in DAYS_OF_WEEK],
                  *[f"{code}_end" for code, _ in DAYS_OF_WEEK],
                  ]

        labels = {
            'start_city': 'Ville de départ',
            'end_city': "Ville d'arrivée",
            'seat_go': 'Nombre de places aller',
            'price': 'Prix',
            'description': "Commentaire",
            'role': 'Rôle',
        }

        widgets = {
            "role": forms.RadioSelect(),
            'monday_active': forms.CheckboxInput(attrs={'class': 'form-check form-switch'}),
            'monday_start': forms.Select(choices=generate_time_choices(), attrs={'class': 'form-select'}),
            "seat_go": forms.Select(choices=[(i, i) for i in range(1, 10)], attrs={'class': 'form-control'}),
            "seat_return": forms.Select(choices=[(i, i) for i in range(0, 10)], attrs={'class': 'form-control'}),
            "price": forms.Select(choices=[(i, i) for i in range(500, 50000, 500)], attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_city'].required = True
        self.fields['end_city'].required = True
        self.fields['seat_go'].required = True
        self.fields['price'].required = True


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        for day_code, _ in DAYS_OF_WEEK:
            field_name = f"{day_code}_active"
            if field_name in self.fields:
                self.fields[field_name].widget = forms.CheckboxInput(
                    attrs={'class': 'form-check-input', 'role': 'switch'}
                )


        self.fields['start_city'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
            'data-search-enabled': 'true',
        })

        self.fields['end_city'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
            'data-search-enabled': 'true',
        })


        self.fields['seat_go'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': 1,
            'default': 1,
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-select js-choice',
            'data-search-enabled': 'true',
            'value': 500,
            'default': 500,
        })

        self.fields['role'].widget.attrs.update({
            'class': 'form-check-input',

        })

        # Radio pour role
        self.fields['role'].widget.attrs.update({'class': 'form-check-input'})

        # Spécifiques js-choice
        for fld in ('start_city', 'end_city', 'seat_go', 'price', 'seat_return'):
            if fld in self.fields:
                self.fields[fld].widget.attrs.update({
                    'class': 'form-select js-choice',
                    'data-search-enabled': 'true',
                })

        # Boucle sur les jours pour appliquer les widgets
        for code, _ in DAYS_OF_WEEK:
            active_f = f"{code}_active"
            if active_f in self.fields:
                self.fields[active_f].widget = forms.CheckboxInput(
                    attrs={'class': 'form-check-input', 'role': 'switch'}
                )
            for suffix in ('start', 'end'):
                tf = f"{code}_{suffix}"
                if tf in self.fields:
                    self.fields[tf].widget = forms.Select(
                        choices=generate_time_choices(),
                        attrs={'class': 'form-select js-choice'}
                    )

    def clean(self):
        cleaned = super().clean()
        # Vérifie qu'au moins un jour est actif
        any_active = False
        for code, _ in DAYS_OF_WEEK:
            if cleaned.get(f"{code}_active"):
                any_active = True
                break
        if not any_active:
            raise ValidationError("Vous devez activer au moins un jour de covoiturage.")
        return cleaned


