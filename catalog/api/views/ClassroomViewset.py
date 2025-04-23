from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action 
from catalog.api.serializers import ClassRoomSerializer
from catalog.models.ClassroomsModel import Classrooms

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classrooms.objects.active()
    permission_clases = [permissions.AllowAny]
    serializer_class = ClassRoomSerializer.ClassRoomSerizlizer

    #search filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search = ['name', 'code']
    ordering_fields = ["created_at", "updated_at","id"]#para filtrar


    #rewrite the destroy method
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        # Retorna una respuesta HTTP 204 (No Content) para indicar éxito
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #function to restore the record
    @action(detail=True, methods=['POST'])#decorador para agregar un endopoint adicional
    def restore(self, request, pk=None):
        try:
            instace = Classrooms.objects.deleted().filter(pk=pk).first()
            if not instace:
                return Response({"message":"No se encontro el registro eliminado", "status":"404"}, status=status.HTTP_404_NOT_FOUND)
            instace.restore()
            return Response({"message":"El registro ha sido restaurado correctamente", "status":"200"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e),"status":"500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

