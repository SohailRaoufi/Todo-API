from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import response

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(CreateAPIView):
    queryset = Todo
    serializer_class = TodoSerializer

    # def post(self, request, format=None):
    #     Data = request.data
    #     todo = Todo.objects.create(
    #         title=Data['title'],
    #         body=Data['body']
    #     )

    #     todo.save()

    #     return response.Response("Data Saved!")


class UpdateTodo(APIView):
    def put(self, request, pk, format=None):
        todo = Todo.objects.get(id=pk)
        serailizer = TodoSerializer(todo, data=request.data)

        if serailizer.is_valid():
            serailizer.save()
            return response.Response("Done")
        return response.Response("Error!")

    def patch(self, request, pk, format=None):
        todo = Todo.objects.get(id=pk)
        serailizer = TodoSerializer(todo, data=request.data, partial=True)

        if serailizer.is_valid():
            serailizer.save()
            return response.Response("Done")
        return response.Response("Error!")


class DeleteTodo(APIView):
    def delete(self, request, pk, format=None):
        todo = Todo.objects.get(id=pk)
        todo.delete()

        return response.Response("Done")
