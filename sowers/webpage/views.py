from multiprocessing import context
from django.shortcuts import render, redirect
from .models import help
from .forms import HelpForm


def home(request):
    return render(request, "webpage/home.html")

def chats(request):
    return render(request, 'webpage/chats.html')

def about(request):
    helps = help.objects.all()
    context = {'helps': helps}  
    return render(request, 'webpage/about.html', context)  

def login(request):
    form = HelpForm()
    if request.method == 'post':
        form = HelpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('about')
    context = {'form': form}
    return render(request, 'webpage/login.html', context)