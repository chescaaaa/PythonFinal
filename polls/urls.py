from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name="polls"),
    path('sample', views.sample, name="template"),
]