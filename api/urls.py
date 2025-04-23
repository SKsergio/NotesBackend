from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('catalog/', include('catalog.api.endpoints', namespace='catalog')),
]
