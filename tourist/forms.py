from django import forms
from .models import Tourist, Booking
from django.forms import ModelForm
from django import forms


class TouristForm(ModelForm):
    class Meta:
        model = Tourist
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'email',
            'phone'
        ]

    def __init__(self, *args, **kwargs):
        super(TouristForm, self).__init__(*args, **kwargs)
        """for field in self.files.values():
            className = 'form-control'
            field.widget.attrs.update({'class': className})"""
        self.fields['password'] = forms.CharField(widget = forms.PasswordInput())
        self.fields['confirm_password'] = forms.CharField(widget = forms.PasswordInput())

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'offer',
            'trip_duration',
        ]

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
