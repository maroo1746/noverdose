from django.urls import path
from . import views
app_name = 'searchmed'

urlpatterns = [
path('', views.home, name='home'),
path('combine/', views.combine, name='combine'),
path('age/', views.age, name='age'),
path('check_medicine/', views.check_medicine, name='check_medicine'),
path('check_contraindication/', views.check_contraindication, name='check_contraindication'),
]