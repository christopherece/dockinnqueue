from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Max, Q



from queues.models import Queue

# Create your views here.
def addqueue(request):
    return render(request, 'dashboard/queue.html')

def submitqueue(request):
    queueIdMax = 0

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        type = request.POST['type']
        status = request.POST['status']
        ritm = request.POST['ritm']

        queueList = Queue.objects.all().count()
        print(queueList)
        if queueList:
            queueIdMax = Queue.objects.aggregate(Max('queue_id'))
            print(queueIdMax)
            addOne = queueList + 1
            appendRitm = 'RITM'
        else:
            addOne = 1

    myqueue = Queue(
        name = name,
        description = description,
        type = type,
        status = status,
        ritm = ritm,
        queue_id = addOne,
    )

    myqueue.save()
    insertedId = queueIdMax

    messages.success(request, 'You are in queue Number {insertedId} ! Thank you and see you')
    return redirect('addqueue')
