from django.shortcuts import render
from item.models import Category, Item
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', context={
        'items': items,
        'categories': categories,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })