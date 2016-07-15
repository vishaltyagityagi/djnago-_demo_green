import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/media/photos')

# Create your models here.
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
    ('STN', 'Staten Island'),
)

class Service(models.Model):
    servicetitle = models.CharField(max_length=100)
    servicedescription = models.TextField(max_length=100,default="")
    # email = models.EmailField(max_length=100,default="")
    is_active = models.BooleanField(default="")
    post_date = models.DateTimeField(default=timezone.now)
    category    = models.CharField(max_length=3, choices=CATEGORIES,default="")
    user    = models.CharField(max_length=3, choices=USER,default="")
    image = models.FileField(upload_to='upload',default="")

    class Meta:
        ordering = ('-post_date',)



class Product(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    is_active = models.BooleanField(default="")
    password = models.CharField(max_length=100,default="")
    repassword = models.CharField(max_length=100,default="")
    post_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='upload',default="")

    class Meta:
        ordering = ('-post_date',)

    # def __unicode__(self):
    #     return '{}'.format(self.firstname)



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

def __str__(self):
    return self.question_text

def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
# def __str__(self):
#     return self.choice_text



class RegistrationForm(models.Model):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password1 = models.CharField(max_length=100, unique=True)
    password2 = models.CharField(max_length=100, unique=True)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='upload')
    flag = models.BooleanField(default='')

    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Blog, self).save()


class Content(models.Model):
    content_name = models.CharField(max_length=100)
    page_url = models.CharField(max_length=100,default="")
    content = models.TextField(default="")
    header = models.TextField(default="")
    footer = models.TextField(max_length=100,default="")
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

class Email(models.Model):
    email_from = models.EmailField(max_length=100,default="")
    to = models.EmailField(max_length=100,default="")
    subject = models.CharField(max_length=100,default="")
    message = models.TextField(default="")


    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

class Cms(models.Model):
    name = models.CharField(max_length=100,default="")
    content = models.CharField(max_length=100,default="")
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

# How we can chnage the table name from database prefix example

# class abc(models.Model):
#     name = models.CharField(max_length=100,default="")
#     content = models.CharField(max_length=100,default="")
#     post_date = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         ordering = ('-post_date',)
#         db_table = "aaaaaa"
