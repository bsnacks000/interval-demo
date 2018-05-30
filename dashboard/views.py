from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    """ render the projects index
    """
    return render(request, 'index.html')
