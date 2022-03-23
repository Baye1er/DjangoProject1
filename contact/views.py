from django.shortcuts import render, redirect
from .forms import CommentForm
from django.contrib import messages
from .models import Comment

# Create your views here.

def blog_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = CommentForm()

    context = {
            'form': form,
        }

    return render(request, 'blog_contact.html', context)



def blog_services(request, *list, **dict):
    #ce block renvoie juste une page html
    #It's under construction

    context = {
        'list': list,
        'dict': dict,
    }

    return render(request, "blog_services.html", context)