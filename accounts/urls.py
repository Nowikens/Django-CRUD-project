from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.register_user, name="register-user"),
    path('login/', views.login_user, name="login-user"),
    path('logout/', views.logout_user, name="logout-user"),
    path('delete/', views.delete_user, name="delete-user"),
    
]
