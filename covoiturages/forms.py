from django import forms
from .models import Covoiturage


def generate_time_choices(interval=30):
    times = []
    for hour in range(24):  # pour 0 à 23 heures
        for minute in range(0, 60, interval):  # intervalle de minutes
            times.append((f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}'))
    return times


class CovoiturageForm(forms.ModelForm):

    monday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    tuesday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    wednesday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    thursday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    friday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    saturday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    sunday_return = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    return_trip = forms.BooleanField(label='Trajet retour', required=False)

    class Meta:
        model = Covoiturage
        fields = ['start_city', 'end_city',

                  'monday_departure', 'monday_return',
                  'tuesday_departure', 'tuesday_return',
                  'wednesday_departure', 'wednesday_return',
                   'thursday_departure', 'thursday_return',
                  'friday_departure', 'friday_return',
                   'saturday_departure', 'saturday_return',
                   'sunday_departure', 'sunday_return',

                  'seat_go', 'seat_back', 'price', 'description']

        labels = {
            'start_city': 'Ville de départ',
            'end_city': "Ville d'arrivée",

            'seat_go': 'Nombre de places aller',
            'seat_back': 'Nombre de places retour',
            'price': 'Prix',
            'description': "Information supplémentaire",

        }

        widgets = {
            "seat_go": forms.Select(choices=[(i, i) for i in range(1, 10)], attrs={'class': 'form-control'}),
            "seat_back": forms.Select(choices=[(i, i) for i in range(0, 10)], attrs={'class': 'form-control'}),
            "price": forms.Select(choices=[(i, i) for i in range(500, 50000, 500)], attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

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

        self.fields['seat_back'].widget.attrs.update({
            'class': 'form-select js-choice',
            'value': 0,
            'default': 0,
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-select js-choice',
            'data-search-enabled': 'true',
            'value': 500,
            'default': 500,
        })

        weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        for day in weeks:
            self.fields[f'{day}_departure'].widget.attrs.update({
                'class': 'form-control flatpickr text-sm-end flatpickr-input time-covoiturage',
                'data-enable-time': 'true',
                'data-no-calendar': 'true',
                'data-date-format': 'H:i',
                'data-time_24hr': 'true',
            })

            self.fields[f'{day}_return'].widget.attrs.update({
                'class': 'form-select js-choice',
                'data-search-enabled': 'true',
            })

