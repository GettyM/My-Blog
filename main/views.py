from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categories, Post
from .forms import ArticleForm, EditArticleForm
from django.urls import reverse_lazy

# ListView and DetailView are inbuilt class-based views


# def home(request):
#     return render(request, 'home.html', {})
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-article_date']


def ClassificationView(request, set):
    category_articles = Post.objects.filter(categories=set)
    # categories is the field on our post model and set is the args in our url path
    return render(request, 'classification.html', {'set': set.title(), 'category_articles': category_articles})


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddArticleView(CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'upload_post.html'
    # we dont add fields when we use form-class
    # fields = '__all__'
    # fields = ('title', 'content')


class CategoriesView(CreateView):
    model = Categories
    template_name = 'categories.html'
    fields = '__all__'


class EditArticleView(UpdateView):
    model = Post
    form_class = EditArticleForm
    template_name = 'update_article.html'


class DeleteArticle(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
