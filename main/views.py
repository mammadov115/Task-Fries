from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


# Create your views here.

@login_required(login_url='sign_in')
def home(request):
    return render(request, 'index.html')


def project_dashboard(request):
    return render(request, "project-dashboard.html")


@login_required(login_url='sign_in')
def task(request):
    form = TaskForm()
    # print(request.POST)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # Form is not valid, get the errors
            errors = form.errors.as_json()
            print(errors)
    return render(request, 'task.html', locals())
