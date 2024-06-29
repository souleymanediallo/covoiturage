from django import forms
from .models import Trip


def generate_time_choices(interval=30):
    times = []
    for hour in range(24):  # pour 0 à 23 heures
        for minute in range(0, 60, interval):  # intervalle de minutes
            times.append((f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}'))
    return times


class TripForm(forms.ModelForm):
    start_time = forms.ChoiceField(choices=generate_time_choices(), label='Heure de départ')
    end_time = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)

    class Meta:
        model = Trip
        fields = ['car', 'start_city', 'end_city', 'start_date',
                  'start_time', 'seat_go', 'price', 'description']
        labels = {
            'car': 'Voiture',
            'start_city': 'Ville de départ',
            'end_city': "Ville d'arrivée",
            'start_date': 'Date de départ',
            'start_time': 'Heure de départ',
            'seat_go': 'Nombre de places',
            'price': 'Prix',
            'description': "Information supplémentaire",
        }
        widgets = {
            "start_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "seat_go": forms.Select(choices=[(i, i) for i in range(1, 6)], attrs={'class': 'form-control'}),
            "price": forms.Select(choices=[(i, i) for i in range(500, 40000, 500)], attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['car'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': '',
        })

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

        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control flatpickr flatpickr-input',
            'type': 'date',
            'data-date-format': "d/m/Y",
            'data-default-date': 'today',
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

        self.fields['start_time'].widget.attrs.update({
            'class': 'form-select js-choice',
            'data-search-enabled': 'true',
        })


