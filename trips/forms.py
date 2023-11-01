from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['user_type', 'trip_type', 'start_city', 'end_city', 'end_time', 'start_date', 'end_date',
                  'start_time', 'seat_go', 'price', 'description', 'luggage']
        labels = {
            'start_city': 'Ville de départ',
            'end_city': "Ville d'arrivée",
            'start_date': 'Date de départ',
            'start_time': 'Heure de départ',
            'seat_go': 'Nombre de places',
            'price': 'Prix',
            'description': "Information supplémentaire",
        }
        widgets = {
            "user_type": forms.RadioSelect(),
            "trip_type": forms.RadioSelect(),
            "start_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "end_time": forms.TimeInput(attrs={'class': 'form-control'}),
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

        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control flatpickr flatpickr-input',
            'type': 'date',
            'data-date-format': 'd/m/Y',
            'data-min-date': 'today',
        })

        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control flatpickr flatpickr-input',
            'type': 'date',
            'data-date-format': 'd/m/Y',
            'data-min-date': 'today',
        })

        self.fields['start_time'].widget.attrs.update({
            'class': 'form-control flatpickr',
            'type': 'time',
            'data-enableTime': "true",
            'data-noCalendar': "true",
            'data-date-format': "H:i",
        })

        self.fields['end_time'].widget.attrs.update({
            'class': 'form-control flatpickr',
            'type': 'time',
            'data-enableTime': "true",
            'data-noCalendar': "true",
            'data-date-format': "H:i",
        })

        self.fields['user_type'].widget.attrs.update({
            'class': 'form-check-input'
        })

        self.fields['trip_type'].widget.attrs.update({
            'class': 'form-check-input'
        })

        self.fields['luggage'].widget.attrs.update({
            'class': 'form-check-input price',
            'id': 'luggage',
            'value': 0,
        })

        self.fields['seat_go'].widget.attrs.update({
            'class': 'form-check-input price',
            'id': 'seat_go',
            'value': 1,
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-check-input price',
            'id': 'price',
            'value': 0,
        })