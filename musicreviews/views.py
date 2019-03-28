from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import MRPost

# Create your views here.


class MusicReviewListView(ListView):
    model = MRPost
    template_name = 'musicreviews.html'


class MusicReviewDetailView(DetailView):
    model = MRPost
    template_name = 'detail_review.html'


class MusicReviewCreateView(CreateView):
    model = MRPost
    template_name = 'new_review.html'
    fields = ['title', 'author', 'body']
