from django.shortcuts import render

# Create your views here.
def addqueue(request):
    return render(request, 'dashboard/queue.html')
