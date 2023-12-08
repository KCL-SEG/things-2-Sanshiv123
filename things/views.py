from django.shortcuts import render
from .forms import ThingsForm

def home(request):
    form = ThingsForm()
    return render(request, 'thing.html', {'form': form})
    #return render(request, 'home.html')

#def thing(request):
    #form = ThingsForm()
    #return render(request, 'thing.html', {'form': form})