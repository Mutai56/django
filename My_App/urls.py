from django.urls import path
from My_App import views


urlpatterns=[
    path('', views.home,name='index'),

    path('about/',views.about,name='about'),
    path('contact/',views.contacts,name='contacts'),

    path('services/', views.services,name='services'),

    path('blog/', views.blog,name='blog'),
    
    path('media/', views.media, name='media')
    ]