from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'prescription/home.html', context={
        'name': 'Fabio Passos',
    })


def contato(request):
    return render(request,'me-apague/temp.html')

def sobre(request):
    return HttpResponse('sobre')