from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Dark Nepal'
        self.fields['email'].widget.attrs['placeholder'] = 'DarkNepal@mail.com'
        self.fields['subject'].widget.attrs['placeholder'] = 'National issue'
        self.fields['message'].widget.attrs['placeholder'] = 'Describe the issue..'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'