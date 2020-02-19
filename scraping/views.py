from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
# Create your views here.

def top(request):
    Datetime = {
        'hour': datetime.now().hour,
    }
    return render(request, 'top.html', Datetime)