from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()

class TodoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def index_view(request):
    return HttpResponse("¡Hola Mundo!")

class TodoRetrieveById(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class TodoDeleteById(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except Exception as e:
            return Response({"message": "No se pudo eliminar"}, status=status.HTTP_400_BAD_REQUEST)
