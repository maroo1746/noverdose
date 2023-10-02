from django.urls import path
from . import views
app_name = 'searchmed'

urlpatterns = [
path('', views.home, name='home'),
path('combine/', views.combine, name='combine')
]