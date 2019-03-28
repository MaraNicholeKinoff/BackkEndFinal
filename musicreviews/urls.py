from django.urls import path
from . import views

urlpatterns = [
    path('musicreviews/', views.MusicReviewListView.as_view(), name='musicreviews'),
    path('post/new_review/', views.MusicReviewCreateView.as_view(), name='new_review'),
    path('post/new_review/<int:pk>/',
         views.MusicReviewDetailView.as_view(), name='detail_review')
]
