from django.urls import path
from . import views




urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('grid', views.grid, name='grid'),
 
]
