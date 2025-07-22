from django.db import models
from catalog.utils.queryset import softDeleteQuerySet #import the queryset to softDelete

class AbstractBaseCatalog(models.Model):
    code = models.CharField(max_length=12, unique=True, null=False)#code 
    name = models.CharField(max_length=50, null=False)#name
    created_at = models.DateTimeField(auto_now_add=True)#field to save date of created
    updated_at = models.DateTimeField(auto_now=True)#field to save updated date
    is_deleted = models.BooleanField(default=False)#field to soft delete

    #queryset return active and delete records
    objects = softDeleteQuerySet.as_manager()#manager expone los datos de queryset

    class Meta():
        abstract = True#con esto indicamos que este modelo es abstracto y por ende no se creara como una tabla en la BD
        ordering = ['id']#indica como deben de ser ordenados los registros al hacer consultas
    
    def __str__(self):
        return f"{self.name}({self.code})"
        
    
    #borrado logico or soft delete in python
    def delete(self, using=None, Keep_parents=False): #debo investigar que son estos metodos
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
    
