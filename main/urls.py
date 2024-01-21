from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('/send_email', views.send_email, name='send_email'),
    path('/contact', views.contact, name='contact'),
    path('/blog', views.blog, name='blog'),
    path('/about', views.about, name='about'),
    path('/staff', views.staff, name='staff'),
    path('/courses', views.courses, name='courses'),
    path('/applyNow', views.applyNow, name='applyNow'),

]