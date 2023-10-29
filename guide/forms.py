from .models import Guide
from django.forms import ModelForm
from django import forms


class GuideSignupForm(ModelForm):
    class Meta:
        model = Guide
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'email',
            'phone',
        ]

    def __init__(self, *args, **kwargs):
        super(GuideSignupForm, self).__init__(*args, **kwargs)
        """for field in self.fields.values():
            className = 'form-control'
            field.widget.attrs.update({'class': className})"""
        self.fields['password'] = forms.CharField(widget = forms.PasswordInput())
        self.fields['confirm_password'] = forms.CharField(widget = forms.PasswordInput())

class GuideEditForm(ModelForm):
    class Meta:
        model = Guide
        fields = [
            'bio',
            'price',
            'location'
        ]

    def __init__(self, *args, **kwargs):
        super(GuideEditForm, self).__init__(*args, **kwargs)
        for field in self.files.values():
            className = 'form-control'
            field.widget.attrs.update({'class': className})
