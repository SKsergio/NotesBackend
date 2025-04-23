from django.db import models
from .base_catalog import AbstractBaseCatalog

class SubjectModel(AbstractBaseCatalog):
    description = models.TextField(max_length=300)

    class Meta():
        db_table = 'mdls_subjects'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
