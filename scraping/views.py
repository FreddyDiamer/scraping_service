from django.shortcuts import render
from .models import Vacancy


menu = [
    { 'title': 'Vacancies', 'url': 'home' }
]

def index(request):
    object_list = Vacancy.objects.all()

    if request.GET :
        city = request.GET.get('city')
        lang = request.GET.get('lang')

        if city:
            object_list = object_list.filter(city__name__contains=city)

        if lang:
            object_list = object_list.filter(lang__name__contains=lang)

    context = {
        'object_list': object_list,
        'menu': menu,
        'current_url': 'home'
    }
    
    return render(request, 'scraping/index.html', context)
