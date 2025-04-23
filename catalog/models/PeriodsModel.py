from django.db import models
from .base_catalog import AbstractBaseCatalog

class PeriodsModel(AbstractBaseCatalog):
    date_from = models.DateField(auto_now=False)
    date_until = models.DateField(auto_now=False)

    class Meta():
        db_table = 'mdls_periods'
        verbose_name = 'period'
        verbose_name_plural = 'periods'

    