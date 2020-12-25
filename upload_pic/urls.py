from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pic, name='upload_pic_homepage'),
]