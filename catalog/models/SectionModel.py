from .base_catalog import AbstractBaseCatalog #import the abstract model

class Section(AbstractBaseCatalog):#model to Sections
    class Meta():
        db_table = 'mdls_sections'
        verbose_name = 'section'
        verbose_name_plural = 'sections'
        ordering = ['created_at']
       