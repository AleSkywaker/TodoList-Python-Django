# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from .models import Todo

# Create your views here.


def index(request):
   # return HttpResponse('Hello World')
   
    todos = Todo.objects.all()[:10]

    context = {
        'titulo':'LISTA DE TAREAS',
       'tareas': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
       'tarea': todo
    }
    return render(request, 'details.html', context)
