from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def top(request):
    Datetime = {
        'hour': datetime.now().hour,
    }
    return render(request, 'top.html', Datetime)




