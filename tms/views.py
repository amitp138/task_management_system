from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
import json

class TasksManagement(APIView):
    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                task = serializer.validated_data
                tasks = self.get_tasks_from_file()
                tasks.append(task)
                self.save_tasks_to_file(tasks)

                return Response({"message": "Task added successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            tasks = self.get_tasks_from_file()

            return Response(tasks, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_tasks_from_file(self):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    
    def save_tasks_to_file(self, tasks):
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
