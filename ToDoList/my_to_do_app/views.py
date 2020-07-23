from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input = request.POST['todoContent']
    todo = Todo(content = user_input, isDone=False)
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    id = request.GET['todoNum']
    todo = Todo.objects.get(id = id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))