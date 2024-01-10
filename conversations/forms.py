from django import forms
from .models import Conversation


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(ConversationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


