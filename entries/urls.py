from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage, name="login"),
    path('home/',views.home,name='home'),
    path('add/<str:user_name>', views.add, name="add"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.LogoutUser, name="logout"),
]
