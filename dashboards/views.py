from django.shortcuts import render
from .models import Dashboard

# Create your views here.
def index(request):
    obj = Dashboard.objects.get(id=1)
    context = {
        'obj' : obj
    }
    return render(request, 'dashboard/index.html', context)

def monitor(request):
    return render(request, 'dashboard/monitor.html')
