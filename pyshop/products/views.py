import django
import django.shortcuts as shortcuts
import django.http as django_http
from .models import Product


def index(request):
    products = Product.objects.all()
    return django.shortcuts.render(request, 'index.html',
                                   {'products': products})


def new(request):
    return django_http.HttpResponse("New Product")