from django.urls import path, include, re_path
from show import views

urlpatterns = [
    #Post Urls
    path('<int:id>/addShowsCategory', views.addShowsCategory.as_view()),
    path('<int:id>/addShowsSubCategory', views.addShowsSubCategory.as_view()),
    path('<int:id>/addShows', views.addShows.as_view()),
    
    #Category
    path('shows_category_js/', views.shows_category_js.as_view(), name='shows_category_js'),
    path('<int:id>/shows_subcategory_js/', views.shows_subcategory_js.as_view(), name='shows_subcategory_js'),

    #ListView Urls
    path('ShowListView', views.ShowListView.as_view()), 

    #Delete Urls
    path('<int:id>/deleteShow/', views.deleteShow.as_view()),
    path('<int:id>/deleteShowsCat/', views.deleteShowsCat.as_view()), 
    path('<int:id>/deleteShowSubCat/', views.deleteShowSubCat.as_view()), 
]