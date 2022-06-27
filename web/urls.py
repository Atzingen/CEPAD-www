from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('services.html', views.services, name='services'),
    path('testimonials.html', views.testimonials, name='testimonials'),
    path('team.html', views.team, name='team'),
]
