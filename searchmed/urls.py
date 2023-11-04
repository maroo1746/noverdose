from django.urls import path
from . import views
app_name = 'searchmed'

urlpatterns = [
path('', views.home_view, name='home'),
path('combine/', views.combine_view, name='combine'),
path('age/', views.age_view, name='age'),
path('check_medicine/', views.check_medicine, name='check_medicine'),
path('check_contraindication/', views.check_contraindication, name='check_contraindication'),
path('log/', views.log_view, name='log'),
path('display_log/', views.display_log, name='display_log'),
]