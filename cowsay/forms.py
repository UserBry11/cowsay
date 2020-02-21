from django import forms
from cowsay.models import Author


class MooForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['text', 'choice']
