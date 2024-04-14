from django.contrib import admin
from django.urls import path, include
from todo_api import views  # Importa views desde todo_api
from  todo_api.views import TodoListCreate
from django.urls import path

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/<int:pk>/', views.TodoRetrieveUpdateDelete.as_view(), name='todo-retrieve-update-delete'),
    path('', views.index_view, name='index'),
    path('api/todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', views.TodoRetrieveById.as_view(), name='todo-retrieve-by-id'),
    path('todos/<int:pk>/delete/', views.TodoDeleteById.as_view(), name='todo-delete-by-id'),
]
