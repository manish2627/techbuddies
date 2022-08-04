
from home import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('userhandler', views.userhandler, name='userhandler'),
    path('handlelogin', views.handlelogin, name='handlelogin'),
    path('handlelogout', views.handlelogout, name='handlelogout'),

]