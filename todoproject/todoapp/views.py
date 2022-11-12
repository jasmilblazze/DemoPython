from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task'
class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'
class taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')
# Create your views here.
def todo(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        Task=task(name=name,priority=priority,date=date)
        Task.save()

    return render(request,'home.html',{'task':Task1})

def delete(request, taskid):
    Task2=task.objects.get(id=taskid)
    if request.method =='POST':
        Task2.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Task':Task})







