from django.shortcuts import render


def index(request):
    return render(request, 'joc/index.html')

def pronostic(request):
    return render(request, 'joc/index.html')

def consulta(request):
    return render(request, 'joc/index.html')

def usuaris(request):
    return render(request, 'joc/index.html')
