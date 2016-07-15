from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import loader, Context, RequestContext
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from green_state.models import Contact
from green_state.models import Support
from green_state.models import Registration



def index(request):
    return render_to_response('index.html' )

# Create your views here.

@csrf_protect
def register(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        # u=request.POST.get('username')
        ex=User.objects.filter(username=request.POST['username']).exists()
        if ex== True:
            return HttpResponseRedirect('/green/username_exist/')

        else:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
                )

                return HttpResponseRedirect('/green/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
def username_exist(request):
    return render_to_response(
    'registration/username_exist.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/green/accounts/login')

@login_required
def home(request):
    req = request.META['PATH_INFO']
    return render_to_response(
    'registration/home.html',
    { 'user': request.user,'req': req}
    )

def about_us(request):

    req = request.META['PATH_INFO']
    return render_to_response(
        'registration/about_us.html', {'req': req}
    )

def contact_us(request):
        # import pdb; pdb.set_trace()
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                form.save()
                form = ContactForm()
                contacts = Contact.objects.all()
            return HttpResponseRedirect('/green/contactsuccess')
        else:
            form = ContactForm()
        contacts = Contact.objects.all()
        req = request.META['PATH_INFO']
        return render_to_response('registration/contact_us.html', {'form': form, 'req': req, 'contacts': contacts}, context_instance=RequestContext(request))

def contactsuccess(request):
        req = request.META['PATH_INFO']
        return render_to_response(
        'registration/contactsuccess.html', {'req': req}
        )

def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)

        if form.is_valid():
            form.save()
            form = SupportForm()
            contacts = Support.objects.all()
        return HttpResponseRedirect('/green/supportsuccess')
    else:
        form = SupportForm()
    supports = Contact.objects.all()
    req = request.META['PATH_INFO']
    return render_to_response('registration/support.html', {'form': form,'req': req, 'supports': supports}, context_instance=RequestContext(request))

def supportsuccess(request):
        req = request.META['PATH_INFO']
        return render_to_response(
        'registration/supportsuccess.html',{'req': req}
        )


# def services(request):
#         return render_to_response(
#         'registration/services.html',
#         )
def solutions(request):
        req = request.META['PATH_INFO']
        return render_to_response(
        'registration/solutions.html',{'req': req}
        )
