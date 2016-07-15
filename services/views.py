from django.shortcuts import render
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
# from green_state.models import Contact
# from green_state.models import Support

# Create your views here.
# def services(request):
#         return render_to_response(
#         'services/service.html',
#         )

def services(request):
        # import pdb; pdb.set_trace()
        if request.method == 'POST':
            form = ServiceForm(request.POST)

            if form.is_valid():
                form.save()
                form = ServiceForm()
                services = Service.objects.all()
            return HttpResponseRedirect('/service')
        else:
            form = ServiceForm()
        services = Service.objects.all()
        req = request.META['PATH_INFO']
        return render_to_response('services/service.html', {'form': form, 'req': req ,'services': services}, context_instance=RequestContext(request))


# def show_service(request):
#     form = ServiceForm()
#     posts = Service.objects.all()
#     return render_to_response('services/service.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
