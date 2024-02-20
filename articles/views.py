from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Articles
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import CommentAddForm
from django.views.generic import CreateView

from django.urls import reverse_lazy, reverse
# Create your views here.

class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = [
        'title',
        'summary',
        'body',
        'photo',
    ]
    template_name = 'article_edit.html'
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk' : self.kwargs['pk']} )
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin, DetailView):
    # Moqolani to'liqligicha ko'rsatish uchun
    model = Articles
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles
    template_name  ='article_new.html'
    fields = (
        'title',
        'summary',
        'body',
        'photo',
    )
    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'pk' : self.kwargs['pk']} )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # user superuser ekanini tekshirish
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
class CommentAddView(CreateView):
    form_class = CommentAddForm
    template_name = 'comment_add.html'

    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'pk' : self.kwargs['pk']} )
    



    
    

