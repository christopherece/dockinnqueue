from asyncore import write
from multiprocessing import context
from unittest import result
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Max, Q
from queues.models import Queue
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from datetime import date, datetime, timedelta


from queues.models import Queue

# Create your views here.
@login_required(login_url='login')
def generate_pdf(request):
    # html = '<html><body>To PDF or not to PDF</body></html>'
    # write_to_file = open('media/test.pdf', "w+b")
    # result = pisa.CreatePDF(html,dest=write_to_file)
    # write_to_file.close()
    # print(result)
    # return HttpResponse(result.err)
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    user = request.user.username
    current_datetime = datetime.now()
    reports = Queue.objects.filter(created__range=[startDate, endDate])
    context = {
        'reports':reports,
        'user':user,
        'current_datetime':current_datetime
        
    }
    html = render_to_string('accounts/report.html', context)
    write_to_file = open('media/test_1.pdf', "w+b")
    result = pisa.CreatePDF(html,dest=write_to_file)
    write_to_file.close()
    return HttpResponse(html)

@login_required(login_url='login')
def updateticket(request, id):
    myqueue = Queue.objects.get(id=id)
    usersList = User.objects.all()

    context = {
        'myqueue':myqueue,
        'usersList':usersList
    }
    return render(request, 'dashboard/updateticket.html', context)

@login_required(login_url='login')
def updatequeue(request, id):
    obj = Queue.objects.get(id = id)
    if request.method == 'POST':
            status = request.POST['status']
            comment = request.POST['comment']
            technician = request.POST['technician']

    obj.status = status
    obj.technician = technician
    obj.comment = comment
    obj.save()
    return redirect('dashboard')

def addqueue(request):
    return render(request, 'dashboard/queue.html')

@login_required(login_url='login')
def submitqueue(request):
    queueIdMax = 0

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        type = request.POST['type']
        status = request.POST['status']
        ritm = request.POST['ritm']
        technician = request.POST['technician']

        if Queue.objects.exists():
            queueList = Queue.objects.filter(status='Active').count()
            queueIdMax = Queue.objects.aggregate(Max('queue_id'))['queue_id__max']
            print(queueIdMax)
            addOne = queueIdMax + 1
        else:
            addOne = 1

    myqueue = Queue(
        name = name,
        description = description,
        type = type,
        status = status,
        ritm = 'RITM'+ritm,
        queue_id = addOne,
        technician = technician,
    )

    myqueue.save()

    messages.success(request, addOne)
    return redirect('addqueue')
