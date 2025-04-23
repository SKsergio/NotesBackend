from rest_framework import viewsets, permissions, filters, status #import the viewset Model
from rest_framework.response import Response
from rest_framework.decorators import action
from catalog.api.serializers import SectionSerializer
from catalog.models.SectionModel import Section


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.active()
    permission_classes = [permissions.AllowAny] #Permitir a todos(Por ahora -_-)
    serializer_class = SectionSerializer.SectionSerializer

    #Search Filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "code"]
    ordering_fields = ["created_at", "updated_at","id"]#para filtrar
    ordering = ["created_at"]

    #rewrite destroy method
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        # Retorna una respuesta HTTP 204 (No Content) para indicar éxito
        return Response(status=status.HTTP_204_NO_CONTENT)

    #function to restore the record
    @action(detail=True, methods=['POST'])#decorador para crear endpount adicional
    def restore(self, request, pk=None):
        try:
            instance = Section.objects.deleted().filter(pk=pk).first()            
            if not instance:
                return Response({"message": "No se encontró el registro eliminado."}, status=status.HTTP_404_NOT_FOUND)
            
            instance.restore()  # Llama al método restore() del modelo
            return Response({"message": "Sección restaurada correctamente."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

