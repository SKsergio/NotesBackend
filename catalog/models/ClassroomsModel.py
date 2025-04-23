from .base_catalog import AbstractBaseCatalog #import the abstract model

class Classrooms(AbstractBaseCatalog):#model to Classrooms
    class Meta():
        db_table = 'mdls_classrooms'
        verbose_name = 'classroom'
        verbose_name_plural = 'classrooms'       