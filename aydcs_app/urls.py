from django.urls import path
from . import views

app_name = 'aydcs_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('cours', views.cours, name='cours'),
    path('a_propos', views.a_propos, name='a_propos'),
    path('galerie', views.galerie, name='galerie'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('portail', views.portail, name='portail'),
    path('message/<str:pk>/', views.message, name='message'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('delete_essai/<str:pk>/', views.delete_essai, name='delete_essai'),
    path('logout', views.logoutPage, name="logout"),
    
]
