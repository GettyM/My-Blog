from django import forms
from .models import Post, Categories

# categories = [('My Software Developer Journey', 'My Software Developer Journey'),
#               ('Travel', 'Travel'), ('Family', "Family"), ('Hiking', 'Hiking'), ('Health Awareness', 'Health Awareness'), ('Leaning Angular', 'Learning Angular')] "This is hard coded data"

categories = Categories.objects.all().values_list('set', 'set')
# this is a model data
categories_list = []

for choice in categories:
    categories_list.append(choice)


class ArticleForm(forms.ModelForm):
    # ModelForm allows us to create form fields for our model
    class Meta:
        model = Post
        fields = ('title', 'title_label', 'categories', 'writer', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_label': forms.TextInput(attrs={'class': 'form-control'}),
            # 'categories': forms.Select(choices=categories, attrs={'class': 'form-control'}),
            'categories': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'writer': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditArticleForm(forms.ModelForm):
    # ModelForm allows us to create form fields for our model
    class Meta:
        model = Post
        fields = ('title', 'title_label', 'categories', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_label': forms.TextInput(attrs={'class': 'form-control'}),
            # 'categories': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
