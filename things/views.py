from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
    #return render(request, 'home.html')

#def thing(request):
    #form = ThingsForm()
    #return render(request, 'thing.html', {'form': form})