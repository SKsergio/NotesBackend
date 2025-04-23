from datetime import date
from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Se guarda automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente en cada cambio

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "Type of person"
        verbose_name_plural = "Types of people"
        ordering = ['name']

class People(models.Model):
    names = models.CharField(max_length=100)
    last_names = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    carnet = models.CharField(max_length=12, null=True, blank=True)
    DUI = models.CharField(max_length=12, unique=True)
    direction = models.TextField(max_length=500, null=True)
    phone = models.IntegerField(null=True)
    photo = models.ImageField(max_length=300, upload_to="people_photos/")
    institution_Role = models.CharField(max_length=255)
    type_Person = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, related_name="people")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Se guarda automáticamente al crear
    updated_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente en cada cambio
    
    #propuety to calculte age based on date
    @property
    def age_person(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day)> (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        return f"{self.names}({self.DUI})"

    class Meta:
        verbose_name ='Person'
        verbose_name_plural = 'People'
        ordering = ['created_at']