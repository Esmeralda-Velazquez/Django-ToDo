from django.contrib import admin
from django.urls import path, include
from todo_api import views  # Importa views desde todo_api
from  todo_api.views import TodoListCreate
from django.urls import path
from todo_api.views import TareaListCreate, TareaDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Tareas",
        default_version='v1',
        description="Documentación de la API de Tareas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/<int:pk>/', views.TodoRetrieveUpdateDelete.as_view(), name='todo-retrieve-update-delete'),
    path('', views.index_view, name='index'),
    path('api/todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', views.TodoRetrieveById.as_view(), name='todo-retrieve-by-id'),
    path('todos/<int:pk>/delete/', views.TodoDeleteById.as_view(), name='todo-delete-by-id'),
     path('tareas/', TareaListCreate.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaDetail.as_view(), name='tarea-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



