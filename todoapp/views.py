from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer

# Todos routes
class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


# Home route
def index(request):
    return render(request, 'base.html')