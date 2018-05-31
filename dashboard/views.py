from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BuildingForm

@login_required
def index_view(request):
    """ render the projects index
    """
    return render(request, 'index.html')

@login_required
def boiler_view(request):
    """ render the projects index
    """
    form = BuildingForm(retrofit_type='Boiler')
    return render(request, 'boiler.html', context={'form':form})

@login_required
def pump_view(request):
    """ render the projects index
    """
    form = BuildingForm(retrofit_type='Pump')
    return render(request, 'pump.html', context={'form':form})
