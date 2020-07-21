from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name="register-user"),
    path('login/', views.LoginUser.as_view(), name="login-user"),
    path('logout/', views.LogoutUser.as_view(), name="logout-user"),
    path('delete/<int:pk>', views.DeleteUser.as_view(), name="delete-user"),
    
]
