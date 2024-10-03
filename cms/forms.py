from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 3, 'name': 'message'}),
        }



THEME_CHOICES = [
    ('default', 'Default'),
    ('dark', 'Dark'),
    ('ocean', 'Ocean'),
    ('forest', 'Forest'),
    ('sunset', 'Sunset'),
]

class ContactFormWithDropdown(forms.ModelForm):
    theme = forms.ChoiceField(
        choices=THEME_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'theme', 'name': 'theme'})
    )
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'theme']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 3, 'name': 'message'}),
        }