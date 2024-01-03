from django.shortcuts import render
import datetime


def index(request):
  context = { 'date': datetime.datetime.now(), 'name': 'Dave' }
  return render(request, 'scraping/index.html', context)