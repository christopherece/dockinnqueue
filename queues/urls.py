from nturl2path import url2pathname
from django.urls import path

from . import views

urlpatterns = [
    path('', views.addqueue, name='addqueue'),
    path('submitqueue', views.submitqueue, name='submitqueue'),

]