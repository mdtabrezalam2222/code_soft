from django.shortcuts import render,redirect
from todo.models import todo


def todo_form(request):
    return render(request,'index.html')
def data(request):
    assignee = request.GET.get('assignee')
    title = request.GET.get('title')
    description = request.GET.get('description')
    status = request.GET.get('status')
    d=todo(assignee=assignee,title=title,description=description,status=status)
    d.save()
    data = todo.objects.all

    """ data={
        "serial":serial,
        "assignee":assignee,
        "title":title,
        "description":description,
        "status":status
    } """
    return render(request,'showData.html',{'data':data})
