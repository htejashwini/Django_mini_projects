from django.shortcuts import render
from .models import Features

def index(request):

    feats = Features.objects.all()

    return render(request, 'index.html', {'feats': feats})
