from builtins import print

from django.db import models
from account.models import User


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ManyToManyField("account.Admin")
    customer = models.ManyToManyField("account.Customer")

    def __str__(self):
        return self.name


class Workspace(models.Model):
    owner = models.ManyToManyField("account.Admin")
    colleague = models.ManyToManyField("account.Colleague")
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TaskCategory(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Task Categories'


class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        HIGHEST = 'highest', 'Highest'
        MEDIUM = 'medium', 'Medium'
        LOW = 'low', 'Low'
        LOWEST = 'lowest', "Lowest"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to=None, max_length=100, blank=True, null=True)
    task_start_date = models.DateTimeField(null=True)
    task_end_date = models.DateTimeField(null=True)
    task_priority = models.CharField(max_length=200, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM)
    description = models.TextField(null=True)

    def __str__(self):
        return self.project.name


class TaskProxy(Task):
    class Meta:
        proxy = True


class AssignedPerson(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user_start_date = models.DateTimeField(null=True, blank=True)
    user_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class AssignedPersonProxy(AssignedPerson):
    class Meta:
        proxy = True
        app_label = 'main'
        verbose_name = 'My Task'
        verbose_name_plural = 'My Tasks'

    def __str__(self):
        return self.task.project.name



