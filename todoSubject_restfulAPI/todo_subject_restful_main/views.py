from .models import TodoList
from .serializers import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

class Todo_subject_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer

class Todo_subject_restful_update(UpdateAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_delete(DestroyAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_create(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoCreateSerializer