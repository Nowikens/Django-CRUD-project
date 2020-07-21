from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('update/<int:pk>', views.UpdateView.as_view(), name="update-post"),
    path('delete/<int:pk>', views.DeletePost.as_view(), name="delete-post"),
]
