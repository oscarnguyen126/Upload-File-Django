from django.urls import path, include
from . import views

urlpatterns = [
  path('UploadFile', views.UploadFile, name='UploadFile'),
]