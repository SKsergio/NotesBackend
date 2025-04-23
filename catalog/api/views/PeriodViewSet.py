from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers.PeriodSerializer import PeriodSerializer
from ...models.PeriodsModel import PeriodsModel

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = PeriodsModel.objects.active()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeriodSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ['date_from', 'date_until', 'id']
    

    def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       instance.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['POST'])
    def restore(self, request, pk=None):
        try:
            instance = PeriodsModel.objects.deleted().filter(pk=pk).first()
            if not instance:
                return Response({"message": "No se encontró el registro eliminado."}, status=status.HTTP_404_NOT_FOUND)
            instance.restore()
            return Response({"message": "Sección restaurada correctamente."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)