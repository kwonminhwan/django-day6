from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    works=Todo.objects.all()
    context = {
        'todo_list': works
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    if request.method=='POST':
        work = request.POST.get('work')
        content = request.POST.get('content')
        is_completed = False

        todo = Todo(work=work, content=content, is_completed=is_completed)
        todo.save()

        return redirect('todos:detail', todo.pk)
    else :

        return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo=Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)


def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method=='POST':
        work = request.POST.get('work')
        content = request.POST.get('content')

        todo.work = work
        todo.content = content
        todo.save()
        return redirect('todos:detail', todo.pk)
    else:
        context = {
            'todo': todo
        }
        return render(request, 'todos/update_todo.html', context)
