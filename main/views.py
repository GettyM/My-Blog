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
    set = Categories.objects.all()
    ordering = ['-article_date']

    def get_context_data(self, *args, **kwargs):
        data_menu = Categories.objects.all()  # data is Categories QuerySet
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["data_menu"] = data_menu
        return context


def CategoriesListView(request, set):
    category_articles = Post.objects.filter(categories=set)
    # categories is the field on our post model and set is the args in our url path
    return render(request, 'categories-list.html', {'set': set.title(), 'category_articles': category_articles})


class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        data_menu = Categories.objects.all()  # data is Categories QuerySet
        context = super(PostDetails, self).get_context_data(*args, **kwargs)
        context["data_menu"] = data_menu
        return context


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

    def get_context_data(self, *args, **kwargs):
        data_menu = Categories.objects.all()  # data is Categories QuerySet
        context = super(CategoriesView, self).get_context_data(*args, **kwargs)
        context["data_menu"] = data_menu
        return context


class EditArticleView(UpdateView):
    model = Post
    form_class = EditArticleForm
    template_name = 'update_article.html'


class DeleteArticle(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
