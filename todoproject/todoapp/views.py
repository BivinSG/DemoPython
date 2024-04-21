import django.shortcuts
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import TodoForm
from .models import Task


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todolist:cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todolist:cbvhome')

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return django.shortcuts.render(request, "home.html", {'task': task1})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return django.shortcuts.redirect('/')
    return django.shortcuts.render(request, "delete.html")


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return django.shortcuts.redirect('/')
    return django.shortcuts.render(request, "edit.html", {'f': f, 'task': task})
