from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactInfo


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ("title", "first_name", "last_name", "country", "phone_number")
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'phone_number': _('Phone Number'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('title', css_class='col-md-2'),
                Div(Field('first_name', placeholder='Enter your first name'), css_class='col-md-5'),
                Div(Field('last_name', placeholder='Enter your last name'), css_class='col-md-5'),
                css_class='form-row'
            ),
            Div(
                Div('country', css_class='col-md-6'),
                Div(Field('phone_number', placeholder='Phone / WhatsApp number'), css_class='col-md-6'),
                css_class='form-row')
        )