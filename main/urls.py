from django.urls import path
from .views import AddArticleView, CategoriesListView, DeleteArticle, EditArticleView, Home, PostDetails, CategoriesView

# we are using as_view function because we are using class based views
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('postdetails/<int:pk>', PostDetails.as_view(), name="postdetails"),
    # pk means post's primary key or id
    # the [name] variable is used to reference the url in the html file
    path('add_article/', AddArticleView.as_view(), name='addarticle'),
    path('postdetails/update/<int:pk>',
         EditArticleView.as_view(), name='editarticle'),
    path('postdetails/<int:pk>/delete',
         DeleteArticle.as_view(), name='deletearticle'),
    path('categories/', CategoriesView.as_view(), name='addcategories'),
    path('categories-list/<str:set>/',
         CategoriesListView, name='categories-list')

]
