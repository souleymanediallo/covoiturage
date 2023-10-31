from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'contact_number', 'user_type', 'password1', 'password2']
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse Email",
            "contact_number": "Numéro de téléphone",
            "user_type": "Vous êtes ?",
            "password1": "Mot de passe",
            "password2": "Confirmer le mot de passe",
        }
        widgets = {
        "user_type": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['user_type'].widget.attrs.update({
            'class': 'form-check-input'
        })

        # self.fields['user_type'].widget.attrs.update({'class': 'form-control form-check-input', 'type': 'radio'})