from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def usuaris(request):
    return render(request, 'joc/index.html')
