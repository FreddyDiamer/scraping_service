from django.shortcuts import render
from .models import Vacancy
from .forms import FilterForm


menu = [
    { 'title': 'Vacancies', 'url': 'home' }
]

def index(request):
    object_list = Vacancy.objects.all()
    form = FilterForm()

    if request.GET :
        city = request.GET.get('city')
        lang = request.GET.get('lang')

        if city:
            object_list = object_list.filter(city__slug=city)

        if lang:
            object_list = object_list.filter(lang__slug=lang)

    context = {
        'object_list': object_list,
        'menu': menu,
        'current_url': 'home',
        'form': form
    }
    
    return render(request, 'scraping/index.html', context)
