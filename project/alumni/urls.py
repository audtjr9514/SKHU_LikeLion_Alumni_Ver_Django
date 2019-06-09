from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('tutors/', views.tutors, name='tutors'),
    path('portfolios/', views.portfolios, name='portfolios')
]
