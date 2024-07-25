# t2/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post2/<int:id>/', views.view_post, name='view_post'),
    path('create2/', views.create_post, name='create_post'),
    path('edit2/<int:id>/', views.edit_post, name='edit_post'),
    path('delete2/<int:id>/', views.delete_post, name='delete_post'),
    path('register2/', views.register, name='register'),
    path('login2/', views.user_login, name='login'),
    path('logout2/', views.user_logout, name='logout'),
]
