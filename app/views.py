from datetime import datetime
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    msg = f'Текущее время: {datetime.now()}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = f"Список файлов в рабочей директории: {listdir()}"
    return HttpResponse(msg)
