from django.urls import path, include, re_path
from movie import views

urlpatterns = [
    #Post Urls
    path('<int:id>/PostMoviesSubCategory', views.PostMoviesSubCategory.as_view()),
    path('<int:id>/PostMoviesCategory', views.PostMoviesCategory.as_view()),
    path('<int:id>/PostMoviesAPI', views.PostMoviesAPI.as_view()),
    path('<int:id>/addMovieGenre', views.addMovieGenre.as_view()),
    path('<int:id>/addMovieProducer', views.addMovieProducer.as_view()),
    path('<int:id>/addMovieReels', views.addMovieReels.as_view()),
    
    #Category
    path('category_js/', views.category_js.as_view(), name='category_js'),
    path('<int:id>/subcategory_js/', views.subcategory_js.as_view(), name='subcategory_js'),
    
    #ListView Urls
    path('MovieListView', views.MovieListView.as_view()),    
    
    #Delete Urls 
    path('<int:id>/deleteMovie/', views.deleteMovie.as_view()),
    path('<int:id>/deleteMovieCat/', views.deleteMovieCat.as_view()),
    path('<int:id>/deleteMovieSubCat/', views.deleteMovieSubCat.as_view()), 
]