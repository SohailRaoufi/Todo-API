from django.urls import path

from .views import DetailTodo, ListTodo

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
]
