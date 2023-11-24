from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'searchmed'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('combine/', views.combine_view, name='combine'),
    path('age/', views.age_view, name='age'),
    path('check_medicine/', views.check_medicine, name='check_medicine'),
    path('check_contraindication/', views.check_contraindication, name='check_contraindication'),
    path('addinfo/', views.addinfo_view, name='addinfo'),
    path('signup/', views.signup_view, name='signup'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]