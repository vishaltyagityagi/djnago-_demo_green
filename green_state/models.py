import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage


state = (
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
cityname = (
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
    ('STN', 'Staten Island'),
)

class Registration(models.Model):
    username = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100)
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    post_date = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=100, choices=state)
    city_Name = models.CharField(max_length=100,choices=cityname)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    pincode = models.CharField(max_length=6)
    password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)
    Is_Active = models.BooleanField(default="")


    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return '{}'.format(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField(max_length=100, default='')
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return '{}'.format(self.id)

class Support(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=100, default='')
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return '{}'.format(self.id)
