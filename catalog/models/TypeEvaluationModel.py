from .base_catalog import AbstractBaseCatalog
from django.db import models

class TypeEvaluationModel(AbstractBaseCatalog):
    description =  models.TextField(max_length=300)

    class Meta():
        db_table = 'mdls_type_evaluations'
        verbose_name = 'typesEvaluation'
        verbose_name_plural = 'typesEvaluation'