from django.shortcuts import render, redirect
from django.contrib import messages
# from django.http import HttpResponse
from .models import Tasks
from .forms import *

# Create your views here.hg
def index(request):
    tasks = Tasks.objects.all()
    form = task_form()

    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('/')
        else:
            messages.error(request, "Error adding task. Please check the form and try again.")
    return render(request, 'tasks/insert.html', context={'tasks':tasks, 'form':form})

def update(request, pk):
    try:
        task = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect('/')
    
    form = task_form(instance=task)
    
    if request.method == "POST":
        form = task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Success: Task has been successfully updated.")
            return redirect('/')
        else:
            messages.error(request, "Error updating task. Please check the form and try again.")
    return render(request, 'tasks/update.html', context={'form': form,})
        
def delete(request, pk):
    try:
        item = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        messages.error(request, "Task not found.")
        return redirect('/')
    
    if request.method == "POST":
        item.delete()
        messages.success(request, "Task has been successfully deleted.")
        return redirect('/')
    
    return render(request, 'tasks/delete.html', context={'item': item})

def toggle_complete(request, pk):
    try:
        task = Tasks.objects.get(id=pk)
        task.complete = not task.complete
        task.save()
        
        status = "completed" if task.complete else "marked as incomplete"
        messages.success(request, f"Task '{task.title}' {status}.")
    except Tasks.DoesNotExist:
        messages.error(request, "Task not found.")
    
    return redirect('/')
