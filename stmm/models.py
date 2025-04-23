from django.db import models

# Create your models here.
#modelo de responsable de los estudiantes
class Responsables():
    names = models.CharField(max_length=55)
    last_names = models.CharField(max_length=55)
    parent = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12, null=True)
    emil = models.EmailField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'responsable'
        verbose_name_plural = 'responsables'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.names}({self.emil})"


#modelo de estudiantes
class Students():
    names = models.CharField(max_length=55)
    last_names = models.CharField(max_length=55)
    email = models.EmailField(max_length=200, unique=True)
    responsable_person = models.ForeignKey(Responsables, on_delete=models.CASCADE, related_name='responsable')
    #llave foranea de detalle grados aca
    
    
