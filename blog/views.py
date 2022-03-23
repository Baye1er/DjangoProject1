from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
from .forms import FormulaireForm
from blog.models import Post, Formulaire
from django.views.generic import FormView, TemplateView, ListView
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib import messages



def blog_index(request):
    posts = Post.objects.all()
    last_posts = Post.objects.all().order_by("-created_on")
    p = Paginator(posts, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        "posts": posts,
        "last_posts": last_posts,
        "page_obj": page_obj,
    }
    return render(request, "blog_index.html", context)





def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog_detail.html", context)



def blog_formulaire(request, pk, formulaire):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormulaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Votre candidature a été bien envoyée, Merci!")
            return redirect('blog_thanks.html')

    else:
        form = FormulaireForm()

    context = {

        "post": post,
        "formulaire": formulaire,
        "form": form,
    }

    return render(request, "blog_formulaire.html", context)



def blog_thanks(request, pk, formulaire, thanks):
    post = Post.objects.get(pk=pk)

    context = {

        "post": post,
        "formulaire": formulaire,
        "thanks": thanks,
    }

    return render(request, "blog_thanks.html", context)



def blog_a_propos(request, *list, **dict):
    #ce block renvoie juste une page html
    #Il est en contruction

    context = {
        'list': list,
        'dict': dict,
    }
    return render(request, "blog_a_propos.html", context)


#Search Classes

class IndexView(ListView):
    template_name = 'base.html'
    page_template = 'blog_index.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.all(),
            'page_title': 'Recherche'
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title_icontains=query)
        else:
            return Post.objects.all()

