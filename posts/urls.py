from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:pk>', views.update_post, name="update-post"),
    path('delete/<int:pk>', views.delete_post, name="delete-post"),
]
