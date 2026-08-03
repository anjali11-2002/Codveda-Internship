from django.shortcuts import render, redirect
from .models import Task


def home(request):

    if request.method == "POST":
        title = request.POST.get("task")

        if title:
            Task.objects.create(title=title)

        return redirect("/")

    tasks = Task.objects.all()

    return render(request, "index.html", {"tasks": tasks})


def complete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.completed = True

    task.save()

    return redirect("/")


def delete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.delete()

    return redirect("/")