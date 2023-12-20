from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'project': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Default select Project Category', 'id': 'project'}),
            'category': forms.Select(attrs={'class': 'form-select', 'aria-label': "Default select Project Category", 'id': 'category'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'id': 'formFileMultipleone', 'multiple': '', }),
            'task_start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'datepickerded', 'type': 'date'}),
            'task_end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'datepickerdedone', 'type': 'date'}),
            'users': forms.Select(attrs={'class': 'form-select', 'multiple aria-label': 'Default select Priority', 'id': 'users'}),
            'task_priority': forms.Select(attrs={'class': 'form-select', 'id': 'task-priority'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea786', 'rows': '3', 'placeholder': 'Add any extra details about the request'})
        }

