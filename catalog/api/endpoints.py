from django.urls import path
from rest_framework import routers
from .views import SectionViewSet, ClassroomViewset, DegreeViewSet, SubjectViewSet, PeriodViewSet, TypeEvaluationViewSet
app_name = "catalog"

routeCatalog = routers.SimpleRouter()
routeCatalog.register('sections', SectionViewSet.SectionViewSet)#route to section catalog 
routeCatalog.register('classrooms', ClassroomViewset.ClassroomViewSet)#route to classrooms catalogs
routeCatalog.register('degrees', DegreeViewSet.DegreeViewSet)#route to degree catalogs
routeCatalog.register('subjects', SubjectViewSet.SubjectViewSet)#route to subject cataloges
routeCatalog.register('periods', PeriodViewSet.PeriodViewSet)#route to types evaluation cataloges
routeCatalog.register('type_evaluations', TypeEvaluationViewSet.TypeEvaluationViewSet)


urlpatterns = routeCatalog.urls
