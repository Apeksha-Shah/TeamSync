from django.urls import path ,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('home',views.home , name='home'),
    path('sign-up',views.sign_up , name='sign_up'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('project',views.project,name = 'project'),
    path('project/<project_code>/', views.project_detail, name='project_detail'),]