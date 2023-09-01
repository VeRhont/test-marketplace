from django.shortcuts import render
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', context={
        'items': items,
        'categories': categories,
    })


def contact(request):
    return render(request, 'core/contact.html')