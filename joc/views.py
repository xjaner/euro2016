from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'joc/index.html')

@login_required
def pronostic(request):
    return render(request, 'joc/index.html')

@login_required
def consulta(request):
    return render(request, 'joc/index.html')

@login_required
def usuaris(request):
    return render(request, 'joc/index.html')
