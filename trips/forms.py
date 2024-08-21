from django import forms
from .models import Trip


def generate_time_choices(interval=30):
    times = []
    for hour in range(24):  # pour 0 à 23 heures
        for minute in range(0, 60, interval):  # intervalle de minutes
            times.append((f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}'))
    return times


class TripForm(forms.ModelForm):
    return_time = forms.ChoiceField(choices=generate_time_choices(), label="Heure de retour", required=False)
    return_trip = forms.BooleanField(label='Trajet retour', required=False)

    class Meta:
        model = Trip
        fields = ['start_city', 'end_city', 'start_date',
                  'start_time', 'return_trip', 'return_date', 'return_time',
                  'seat_go', 'seat_back', 'price', 'description']
        labels = {
            'start_city': 'Ville de départ',
            'end_city': "Ville d'arrivée",
            'start_date': 'Date de départ',
            'start_time': 'Heure de départ',
            'seat_go': 'Nombre de places aller',
            'seat_back': 'Nombre de places retour',
            'price': 'Prix',
            'description': "Information supplémentaire",
            'return_trip': 'Trajet retour',
            'return_date': 'Date de retour',
            'return_time': 'Heure de retour',
        }

        widgets = {
            "start_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "return_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "seat_go": forms.Select(choices=[(i, i) for i in range(1, 10)], attrs={'class': 'form-control'}),
            "seat_back": forms.Select(choices=[(i, i) for i in range(0, 10)], attrs={'class': 'form-control'}),
            "price": forms.Select(choices=[(i, i) for i in range(500, 50000, 500)], attrs={'class': 'form-control'}),

            "return_trip": forms.CheckboxInput(attrs={
                'class': 'form-check-input flex-shrink-0',
                'id': 'id_return_trip',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Vérifiez si l'heure existe avant d'essayer de la formater
        if self.instance.start_time:
            self.fields['start_time'].initial = self.instance.start_time.strftime('%H:%M:%S')
        else:
            self.fields['start_time'].initial = ''  # ou une autre valeur par défaut

        if self.instance.return_date:
            self.fields['return_date'].initial = self.instance.return_date

        if self.instance.return_time:
            self.fields['return_time'].initial = self.instance.return_time.strftime('%H:%M:%S')
        else:
            self.fields['return_time'].initial = ''  # ou une autre valeur par défaut

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

        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control flatpickr flatpickr-input',
            'type': 'date',
            'data-date-format': "d/m/Y",
        })

        self.fields['return_date'].widget.attrs.update({
            'class': 'form-control flatpickr flatpickr-input',
            'type': 'date',
            'data-date-format': "d/m/Y",
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

        self.fields['start_time'].widget.attrs.update({
            'class': 'form-control flatpickr text-sm-end flatpickr-input',
            'data-enable-time': 'true',
            'data-no-calendar': 'true',
            'data-date-format': 'H:i',
            'data-time_24hr': 'true',
        })

        self.fields['return_time'].widget.attrs.update({
            'class': 'form-select js-choice',
            'data-search-enabled': 'true',
        })

        self.fields['return_trip'].widget.attrs.update({
            'class': 'form-check-input form-check-input flex-shrink-0',
            'role': 'switch',
            'id': "id_return_trip"
        })

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if start_time == "00:00":
            return self.instance.start_time  # Renvoyer l'heure actuelle si "00:00" est détecté
        return start_time

    def clean_return_time(self):
        return_time = self.cleaned_data.get('return_time')
        if return_time == "00:00":
            return self.instance.return_time  # Renvoyer l'heure actuelle si "00:00" est détecté
        return return_time


