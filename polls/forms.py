import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.forms import ModelForm
from .models import RegistrationForm
from .models import Blog,Product,Service,Content,Email,Cms


CATEGORIES = (
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
USER = (
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
)


class ServiceForm(ModelForm):
    error_css_class = 'error'

    category = forms.ChoiceField(choices=CATEGORIES, required=True )
    user = forms.ChoiceField(choices=USER, required=True )

    class Meta:
        model = Service
        fields = ('servicetitle', 'servicedescription','image','is_active','category','user', )

    widgets = {
            'servicetitle': forms.TextInput(attrs={'placeholder': 'What\'s your title?'}),
            'servicedescription': forms.TextInput(attrs={'placeholder': 'Please enter description'})
        }




class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'body','image', )


class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationForm
        fields = ('username', 'email','password1', 'password2',)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('firstname','lastname','is_active','image', 'email',)

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ('content_name','page_url','content','header', 'footer',)

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email_from','to','subject','message',)

class CmsForm(ModelForm):
    class Meta:
        model = Cms
        fields = ('name','content',)


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
