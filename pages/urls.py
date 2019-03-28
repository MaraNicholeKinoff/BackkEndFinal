from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('ourteam/', views.TeamPageView.as_view(), name='ourteam'),
]
