from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers.SubjectSerializer import SubjectSerializer
from ...models.SubjectsModel import SubjectModel


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.active()#obtenemos solamente los registros que se encuntran activos
    permission_classes = [permissions.AllowAny]
    serializer_class = SubjectSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ["created_at", "updated_at","id"]#para filtrar

    #rewrite destroy method
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #FUNCTION TO RESTORE THE RECORD
    @action(detail=True, methods=['POST'])
    def restore(self, request, pk=None):
        try:
            instance = SubjectModel.objects.deleted().filter(pk=pk).first()
            if not instance:
                return Response({"message": "No se encontró el registro eliminado."}, status=status.HTTP_404_NOT_FOUND)
            instance.restore()
            return Response({"message": "Sección restaurada correctamente."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)