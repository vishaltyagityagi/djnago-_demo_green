from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Service(models.Model):
    rent_service = models.TextField(max_length=2000, default='')
    public_service = models.TextField(max_length=2000)
    booking = models.TextField(max_length=2000)
    renting = models.TextField(max_length=2000)
    home_loan = models.TextField(max_length=2000, default='')
    transport_service = models.TextField(max_length=2000, default='')
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return '{}'.format(self.id)
