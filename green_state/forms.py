import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.forms import ModelForm
from .models import Registration
from .models import Contact
from .models import Support





class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ('email','username', 'first_Name','last_Name', 'address','pincode','phone','state','city_Name','password','Confirm_Password','Is_Active')

def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

def clean(self):
    if 'password' in self.cleaned_data and 'Confirm_Password' in self.cleaned_data:
        if self.cleaned_data['password'] != self.cleaned_data['Confirm_Password']:
            raise forms.ValidationError(_("The two password fields did not match."))
    return self.cleaned_data


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','phone','message')

class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ('name','description')
