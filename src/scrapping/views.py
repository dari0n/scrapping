from django.shortcuts import render
from .models import Vacancy
# Create your views here.


def home_view(request):
    objects_list = Vacancy.objects.all()
    return render(request, 'scrapping/home.jinja2', {'objects_list' : objects_list})