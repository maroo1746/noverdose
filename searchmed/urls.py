from django.urls import path
from . import views
app_name = 'searchmed'

urlpatterns = [
path('', views.home_view, name='home'),
path('combine/', views.combine_view, name='combine'),
path('age/', views.age_view, name='age'),
]