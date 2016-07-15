import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.forms import ModelForm
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('rent_service','public_service','booking','renting','home_loan','transport_service')
