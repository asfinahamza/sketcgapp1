from django.urls import path, include, re_path
from api import views

urlpatterns = [
    
    #Post Urls
    path('addLiveLink', views.addLiveLink.as_view()),
]