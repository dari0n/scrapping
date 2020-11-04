from django.shortcuts import render
from .models import Vacancy
# Create your views here.


def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    objects_list = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if language:
            _filter['language__name'] = language
        
        objects_list = Vacancy.objects.filter(**_filter)

    return render(request, 'scrapping/home.html', {'objects_list' : objects_list})