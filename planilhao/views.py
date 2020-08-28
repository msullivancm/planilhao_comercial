from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
def find(request):
    form = ImpressoraForm
    return render(request, 'findform.html', {'form':form})