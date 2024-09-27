from django.urls import path

from .views import DetailTodo, ListTodo, CreateTodo, DeleteTodo, UpdateTodo

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
    path("create/", CreateTodo.as_view(), name="create_todo"),
    path("delete/<int:pk>", DeleteTodo.as_view(), name="delete_todo"),
    path("update/<int:pk>", UpdateTodo.as_view(), name="update_todo"),

]
