from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

app_name = 'searchmed'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('combine/', views.combine_view, name='combine'),
    path('add_med_user/', views.add_med_user_view, name='add_med_user'),
    path('age/', views.age_view, name='age'),
    path('check_medicine/', views.check_medicine, name='check_medicine'),
    path('check_contraindication/', views.check_contraindication, name='check_contraindication'),
    path('addinfo/', views.addinfo_view, name='addinfo'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='searchmed:home'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user_med/', views.user_med_view, name='user_med'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]