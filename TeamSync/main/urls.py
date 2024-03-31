from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('home',views.home , name='home'),
    path('sign-up',views.sign_up , name='sign_up'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('project',views.project,name = 'project'),
 path('project/<int:project_code>/', views.project_detail, name='project_detail'),]