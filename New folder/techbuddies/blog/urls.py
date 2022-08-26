from blog import views
from django.urls import path, include

urlpatterns = [
    path('comment', views.comment, name='comment'),
    path('', views.blogHome, name='blogHome'),
    path('blogpost<str:slug>', views.blogPost, name='blogPost'),

]