from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import PicTweetModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class PicList(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = PicTweetModel


class PicDetail(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = PicTweetModel
    context_object_name = 'item'


class PicCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = PicTweetModel
    fields = (
        'title',
        'coment',
        'pic',
        'author',
    )
    success_url = reverse_lazy('tweetapp:list')


class PicDelete(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = PicTweetModel
    context_object_name = 'item'
    success_url = reverse_lazy('tweetapp:list')


class PicUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'update.html'
    model = PicTweetModel
    fields = (
        'title',
        'coment',
        'pic',
    )
    success_url = reverse_lazy('tweetapp:list')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'