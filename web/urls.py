from django.urls import path, include, re_path
from web import views

urlpatterns = [
    #Auth Urls
    path('signin/', views.signin.as_view(),name="signin"),
    path('signout/', views.signoutpg.as_view(),name="signout"),
    path('signinpg', views.signinpg.as_view(),name="signinpg"),
    path('logout/', views.logoutpg.as_view(),name="logout"),

    #Main Urls
    path('', views.index.as_view(),name="home"),
    path('about/', views.about.as_view(),name="about"),
    path('movies/', views.movies.as_view()),
    path('<int:id>/moviesDetails/', views.moviesDetails.as_view()),
    path('shows/', views.shows.as_view()),
    path('<int:id>/showsDetails/', views.showsDetails.as_view()),
    path('blogs/', views.blogs.as_view()),
    path('<int:id>/blogDetail/', views.blogDetail.as_view()),
    path('contact/', views.contact.as_view()),
    path('pricing/', views.pricing.as_view()),
    path('<int:id>/myprofile/', views.myprofile.as_view()),
    path('<int:id>/viewProfile/', views.viewProfile.as_view()),
    path('settings/', views.mySettings.as_view()),
    path('allShows/', views.allShows.as_view()),
    path('privacy/', views.privacy.as_view()),
    path('terms/', views.terms  .as_view()),
    
    #Dashboard Urls
    path('dashboard/', views.dashboard.as_view(),name="dashboard"),
    path('userlist/', views.userlist.as_view(),name="userlist"),
    path('<int:id>/addlivelink/', views.addlivelink.as_view(),name="addlivelink"),
    path('<int:id>/addmovie/', views.addmovie.as_view()),
    path('movielist/', views.movielist.as_view(),name="movielist"),
    path('<int:id>/addmoviecategory/', views.addmoviecategory.as_view()),
    path('moviecategorylist/', views.moviecategorylist.as_view(),name="moviecategorylist"),
    path('<int:id>/addmoviesubcategory/', views.addmoviesubcategory.as_view()),
    path('moviesubcategorylist/', views.moviesubcategorylist.as_view(),name="moviesubcategorylist"),
    path('<int:id>/addgenre/', views.addgenre.as_view()),
    path('genrelist/', views.genrelist.as_view(),name="genrelist"),
    path('<int:id>/addproducer/', views.addproducer.as_view()),
    path('producerlist/', views.producerlist.as_view(),name="producerlist"),
    path('<int:id>/addreels/', views.addreels.as_view()),
    path('reelslist/', views.reelslist.as_view(),name="reelslist"),
    
    path('<int:id>/addshowscategory/', views.addshowscategory.as_view()),
    path('showscategorylist/', views.showscategorylist.as_view(),name="showscategorylist"),
    path('<int:id>/addshowssubcategory/', views.addshowssubcategory.as_view()),
    path('showssubcategorylist/', views.showssubcategorylist.as_view(),name="showssubcategorylist"),
    path('<int:id>/addshow/', views.addshow.as_view()),
    path('showslist/', views.showslist.as_view()),
        
    #Post Urls
    path('<int:id>/PostProfile', views.PostProfile.as_view()),
    path('PostMessage', views.PostMessage.as_view()),
    path('postBlog', views.postBlog.as_view()),
    
    #ListView Urls
    path('MessagesListView', views.MessagesListView.as_view()),
    path('BlogListView', views.BlogListView.as_view()), 
    
    #Api View
    path('<int:id>/BlogDetailAPIView/', views.BlogDetailAPIView.as_view()),
    
    #Delete Routes
    path('<int:id>/DeleteProfile/', views.DeleteProfile.as_view()),
    
]