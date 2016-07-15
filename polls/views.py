from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Question
from django.http import Http404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from polls.models import Blog
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView,DetailView
# from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from polls.models import Product
from polls.models import Service
from polls.models import Content
from polls.models import Email






class PostListView(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = BlogForm()
    posts = Blog.objects.all()
    template_name = ('polls/index.html')

class ProductListView(ListView):
    # import pdb; pdb.set_trace()
    queryset = Product.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = ProductForm()
    template_name = ('user/user_index.html')

class ServiceListView(ListView):
    # import pdb; pdb.set_trace()
    queryset = Service.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = ServiceForm()
    template_name = ('service/service_index.html')

class ContentListView(ListView):
    queryset = Content.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = ContentForm()
    posts = Content.objects.all()
    template_name = ('content/content_index.html')

class EmailListView(ListView):
    queryset = Email.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = EmailForm()
    posts = Email.objects.all()
    template_name = ('email/email_index.html')

class CmsListView(ListView):
    queryset = Cms.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    form = CmsForm()
    posts = Cms.objects.all()
    template_name = ('cms/cms_index.html')




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def admin_blank(request):
    return render_to_response('admin_blank.html',)



def delete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = BlogForm(request.POST, request.FILES)
    # newdoc = Blog(image = request.FILES['image'])
    # newdoc.save()

    if form.is_valid():
        form.save()
        form = BlogForm()
    else:
        form = BlogForm()
        posts = Blog.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Blog.objects.filter(id=run).delete()
    # return render_to_response('polls/index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/home')



def userdelete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = BlogForm(request.POST, request.FILES)
        posts = Product.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Product.objects.filter(id=run).delete()
    # return render_to_response('user/user_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/usermanagement')



def servicedelete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = ServiceForm(request.POST, request.FILES)
        posts = Service.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Service.objects.filter(id=run).delete()
    # return render_to_response('service/service_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/servicemanagement')

def contentdelete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = ContentForm(request.POST, request.FILES)
        posts = Content.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Content.objects.filter(id=run).delete()
    # return render_to_response('service/service_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/contentmanagement')

def emaildelete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = EmailForm(request.POST, request.FILES)
        posts = Email.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Email.objects.filter(id=run).delete()
    # return render_to_response('service/service_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/emailmanagement')


def cmsdelete(request):
    # import pdb; pdb.set_trace()
    if request.method == 'GET':
        form = CmsForm(request.POST, request.FILES)
        posts = Cms.objects.all()
    run_list = request.GET.getlist('chk_id[]')
    for run in run_list:
        run = int(run)
        Cms.objects.filter(id=run).delete()
    # return render_to_response('service/service_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
    return HttpResponseRedirect('/cmsmanagement')







def new_product(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        # newdoc = Blog(image = request.FILES['image'])
        # newdoc.save()
        if form.is_valid():
            form.save()
            form = BlogForm()
            posts = Blog.objects.all()
        # return render_to_response('polls/index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
        return HttpResponseRedirect('/home')


    else:
        form = BlogForm()
    posts = Blog.objects.all()
    return render_to_response('registration/new_product.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))



def new_service(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ServiceForm()
            posts = Service.objects.all()
        return HttpResponseRedirect('/servicemanagement')


    else:
        form = ServiceForm()
    posts = Service.objects.all()
    return render_to_response('service/new_service.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

def new_content(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ContentForm()
            posts = Content.objects.all()
        return HttpResponseRedirect('/contentmanagement')


    else:
        form = ContentForm()
    posts = Content.objects.all()
    return render_to_response('content/new_content.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))



def new_user(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ProductForm()
            posts = Product.objects.all()
        return HttpResponseRedirect('/usermanagement')

            # return render_to_response('user/user_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

    else:
        form = ProductForm()
    posts = Product.objects.all()
    return render_to_response('user/new_user.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))


def new_email(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = EmailForm()
            posts = Email.objects.all()
        return HttpResponseRedirect('/emailmanagement')


    else:
        form = EmailForm()
    posts = Email.objects.all()
    return render_to_response('email/new_email.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

def new_cms(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = CmsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = CmsForm()
            posts = Cms.objects.all()
        return HttpResponseRedirect('/cmsmanagement')


    else:
        form = CmsForm()
    posts = Cms.objects.all()
    return render_to_response('cms/new_cms.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))





def index(request):
    form = BlogForm()
    posts = Blog.objects.all()
    return render_to_response('polls/index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
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

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def search(request):

        q = request.GET['q']
        results = Blog.objects.filter(title__contains=q) | \
                Blog.objects.filter(body__contains=q) | \
                Blog.objects.filter(slug__contains=q)
        return render_to_response('polls/index.html', {'results':results, 'q':q})



def service(request):
     return render_to_response('service/service_home.html')





def usermanagement(request):
    form = ProductForm()
    posts = Product.objects.all()
    return render_to_response('user/user_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

def servicemanagement(request):
    form = ServiceForm()
    posts = Service.objects.all()
    return render_to_response('service/service_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

def contentmanagement(request):
    form = ContentForm()
    posts = Content.objects.all()
    return render_to_response('content/content_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))


def emailmanagement(request):
    form = EmailForm()
    posts = Email.objects.all()
    return render_to_response('email/email_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))

def cmsmanagement(request):
    form = CmsForm()
    posts = Cms.objects.all()
    return render_to_response('cms/cms_index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))





def usersearch(request):
        q = request.GET['q']
        results = Product.objects.filter(firstname__contains=q) | \
                Product.objects.filter(lastname__contains=q)
        return render_to_response('user/user_index.html', {'results':results, 'q':q})

def servicesearch(request):
        q = request.GET['q']
        results = Service.objects.filter(servicetitle__contains=q) | \
                Service.objects.filter(servicedescription__contains=q)
        return render_to_response('service/service_index.html', {'results':results, 'q':q})

def contentsearch(request):
        q = request.GET['q']
        results = Content.objects.filter(content_name__contains=q) | \
                Content.objects.filter(content__contains=q)
        return render_to_response('content/content_index.html', {'results':results, 'q':q})

def emailsearch(request):
        q = request.GET['q']
        results = Email.objects.filter(email_from__contains=q) | \
                Email.objects.filter(subject__contains=q)
        return render_to_response('email/email_index.html', {'results':results, 'q':q})

def cmssearch(request):
        q = request.GET['q']
        results = Cms.objects.filter(name_from__contains=q) | \
                Cms.objects.filter(content__contains=q)
        return render_to_response('cms/cms_index.html', {'results':results, 'q':q})




def edit(request, post_id=None):
    instance = get_object_or_404(Blog, id=post_id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/home')

    context = {
    	"title": instance.title,
    	"instance": instance,
    	"form":form,
        "posts" : Blog.objects.all(),

    }
    return render(request, "registration/edit_product.html", context)


def edit_user(request, post_id=None):
    instance = get_object_or_404(Product, id=post_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/usermanagement')

    context = {
    	"firstname": instance.firstname,
    	"instance": instance,
    	"form":form,
        "posts" : Product.objects.all(),
        # "posts":Product.objects.get(id=12),

    }
    return render(request, "registration/edit_user.html", context)


def show_product(request, post_id=None):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'registration/show.html', {'post': post})

def show_user(request, post_id=None):
    post = get_object_or_404(Product, id=post_id)
    return render(request, 'registration/show_user.html', {'post': post})


def show_service(request, post_id=None):
    post = get_object_or_404(Service, id=post_id)
    return render(request, 'registration/show_service.html', {'post': post})

def show_content(request, post_id=None):
    post = get_object_or_404(Content, id=post_id)
    return render(request, 'registration/show_content.html', {'post': post})

def show_email(request, post_id=None):
    post = get_object_or_404(Email, id=post_id)
    return render(request, 'registration/show_email.html', {'post': post})

def show_cms(request, post_id=None):
    post = get_object_or_404(Cms, id=post_id)
    return render(request, 'registration/show_cms.html', {'post': post})








def edit_service(request, post_id=None):
    instance = get_object_or_404(Service, id=post_id)
    form = ServiceForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/servicemanagement')

    context = {
    	"servicetitle": instance.servicetitle,
    	"instance": instance,
    	"form":form,
        "posts" : Service.objects.all(),
        # "posts":Product.objects.get(id=12),

    }
    return render(request, "registration/edit_service.html", context)


def edit_content(request, post_id=None):
    instance = get_object_or_404(Content, id=post_id)
    form = ContentForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/contentmanagement')

    context = {
    	"content_name": instance.content_name,
    	"page_url": instance,
    	"form":form,
        "posts" : Content.objects.all(),
        # "posts":Product.objects.get(id=12),

    }
    return render(request, "registration/edit_content.html", context)

def edit_email(request, post_id=None):
    instance = get_object_or_404(Email, id=post_id)
    form = EmailForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/emailmanagement')

    context = {
    	"email_from": instance.email_from,
    	"to": instance,
    	"form":form,
        "posts" : Email.objects.all(),
        # "posts":Product.objects.get(id=12),

    }
    return render(request, "registration/edit_email.html", context)

def edit_cms(request, post_id=None):
    instance = get_object_or_404(Cms, id=post_id)
    form = CmsForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
    	instance = form.save(commit=False)
    	instance.save()
    	return HttpResponseRedirect('/cmsmanagement')

    context = {
    	"name": instance.name,
    	"content": instance,
    	"form":form,
        "posts" : Cms.objects.all(),
        # "posts":Product.objects.get(id=12),

    }
    return render(request, "registration/edit_cms.html", context)
