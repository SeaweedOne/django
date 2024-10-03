from .models import Todo as redistodo
from .serializers import TodoSerializer
from .cache_function import invalidate_todo_cache



def create(data):
    serializer = TodoSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def get():
    Todo = redistodo.objects.all()
    serializer = TodoSerializer(Todo, many=True)
    return serializer.data


def add(request):
    serializer = TodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    invalidate_todo_cache()
    return serializer.data


def update(request, pk=None):
    updateTodo = redistodo.objects.get(id=pk)
    serializer = TodoSerializer(instance=updateTodo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.data


def remove(request, pk=None):
    Todo = redistodo.objects.get(id=pk)
    Todo.delete()
    return "deleted"