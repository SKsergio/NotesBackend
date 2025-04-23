from .base_catalog import AbstractBaseCatalog

class DegreesModel(AbstractBaseCatalog):
     class Meta():
        db_table = 'mdls_degrees'
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'  