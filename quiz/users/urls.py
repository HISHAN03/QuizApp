from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.My_login, name="My_login"),
    path('/staff_signup', views.staff_signup, name="staff_signup"),
    path('quizz',views.quiz_list,name="quiz_list"),
    path('questions/<int:quiz_id>/', views.questions, name='questions'),
    path('delet_quiz/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    path('exist/<int:quiz_id>/', views.exist, name='exist'),
    path('staff_quiz_list/',views.staff_quiz_list,name="staff_quiz_list"),
    path('staff/',views.staff_login,name="staff_login"),
    path('create/',views.create,name="create"),
    path('add-value-to-database/', views.add_value_to_database_view, name='add_value_to_database'),
    path('add-New-value-to-database/', views.add_New_value_to_database_view, name='add_New_value_to_database'),
    path("register/", views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update_score/', views.update_score, name='update_score'),
]
