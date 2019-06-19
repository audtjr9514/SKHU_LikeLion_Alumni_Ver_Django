from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member', views.members, name='members'),
    path('tutor', views.tutors, name='tutors'),
    path('portfolio', views.portfolios, name='portfolios')
]
