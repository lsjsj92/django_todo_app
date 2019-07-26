from .models import TodoList
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date', 'is_complete')