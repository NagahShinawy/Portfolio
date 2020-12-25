from django.urls import path
from .views import home, project_details

app_name = 'portfolio'

urlpatterns = [
    path('', home, name='home'),
    path('project_details/<str:slug>', project_details, name='project_details'),
]