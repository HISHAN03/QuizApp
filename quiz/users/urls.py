from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.My_login, name="My_login"),
    path('quizz',views.quiz_list,name="quiz_list"),
    path('questions/<int:quiz_id>/', views.questions, name='questions'),
    path('exist/<int:quiz_id>/', views.exist, name='exist'),
    path('staff/',views.staff_quiz_list,name="staff_quiz_list"),
    path('create/',views.create,name="create"),
    path('add-value-to-database/', views.add_value_to_database_view, name='add_value_to_database'),
    path('add-New-value-to-database/', views.add_New_value_to_database_view, name='add_New_value_to_database'),
    path("register/", views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
