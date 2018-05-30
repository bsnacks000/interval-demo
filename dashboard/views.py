from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    """ render the projects index
    """
    return render(request, 'index.html')


@login_required
def boiler_chart_view(request):
    """ render the boiler chart template
    """
    return render(request, 'boiler.html')


@login_required
def pump_chart_view(request):
    """ render the pump_chart_view
    """
    return render(request, 'pump.html')
