from django.shortcuts import render


def home(request):
    return render(request, 'prescription/home.html', context={
        'name': 'Fabio Passos',
    })

