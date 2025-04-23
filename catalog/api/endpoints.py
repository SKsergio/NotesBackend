from django.urls import path
from rest_framework import routers
from .views import SectionViewSet, ClassroomViewset, DegreeViewSet, SubjectViewSet, PeriodViewSet, TypeEvaluationViewSet
app_name = "catalog"

routeCatalog = routers.SimpleRouter()
routeCatalog.register('section', SectionViewSet.SectionViewSet)#route to section catalog 
routeCatalog.register('classrooms', ClassroomViewset.ClassroomViewSet)#route to classrooms catalogs
routeCatalog.register('degree', DegreeViewSet.DegreeViewSet)#route to degree catalogs
routeCatalog.register('subject', SubjectViewSet.SubjectViewSet)#route to subject cataloges
routeCatalog.register('period', PeriodViewSet.PeriodViewSet)#route to types evaluation cataloges
routeCatalog.register('type_evaluation', TypeEvaluationViewSet.TypeEvaluationViewSet)


urlpatterns = routeCatalog.urls
