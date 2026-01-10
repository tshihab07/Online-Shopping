from django.shortcuts import render, redirect
from  django.contrib.auth import login
from item.models import Category, Item
from .form import RegisterForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html',
                {'categories': categories,
                 'items': items},
                )


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            return redirect('login/')
    
    else:
        form = RegisterForm()
    
    return render(request, "signup.html", {
        "form": form
    })
