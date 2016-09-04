from django.shortcuts import render
from django.http import HttpResponse

from .models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    # Construct a dictionary to pass to the template
    context_dict = {'categories': category_list}

    # Return a rendered response
    return render(request, 'bassist/index.html', context=context_dict)

def about(request):
    return render(request, 'bassist/about.html')