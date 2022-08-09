from django.urls import path

from . import views

urlpatterns = [
    path('', views.addqueue, name='addqueue'),
    path('submitqueue', views.submitqueue, name='submitqueue'),
    path('updateticket/<uuid:id>/', views.updateticket, name='updateticket'),
    path('updatequeue/<uuid:id>/', views.updatequeue, name='updatequeue'),

]