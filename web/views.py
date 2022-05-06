from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, request
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.models import User
import requests
import json
from rest_framework import authentication
from rest_framework.views import APIView
from django.views.generic import ListView

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView  
from rest_framework import viewsets, status
from rest_framework import generics, permissions, pagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

#authentication helpers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate,logout, login
from django.contrib import messages
#from web.serializers import *
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser

from web.forms import *
from web.models import *
from web.serializers import *
from movie.models import *
from show.models import*
from api.models import *

class CompanyPagination(pagination.PageNumberPagination):
    page_size = 9

    
##### Auth View #####
#####################
class signin(APIView):
    def get(self, request):
        form=LoginForm()
        return render(request, 'web/login.ejs',{'form':form})

class signoutpg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        logout(request)
        return redirect('/signin')

class logoutpg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        logout(request)
        print("done")
        return redirect('/')

class signinpg(APIView):
    def post(self,request):
        form = LoginForm()
        user = authenticate(
            username=request.POST['name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(reverse('dashboard'))
            else:
                return redirect(reverse('signin'))
        context = {
            'error':"Invalid Credential",
            'form': form
        }
        return render(request, 'web/login.ejs', context=context)
    

##### Main View #####
#####################
class index(APIView):
    def get(self, request):
        return render(request, 'web/index.ejs')
  
class about(APIView):
    def get(self, request):
        return render(request, 'web/about.ejs')
      
class movies(APIView):
    def get(self, request):
        context = {
            "movies": Movies.objects.all().order_by('-id'),
            "catg":MovieCategory.objects.all().order_by('-id')
        }
        return render(request, 'web/movies.ejs', context=context)
    
class moviesDetails(APIView):
    def get(self, request, *args, **kwargs):
        context = {
            'movies' : self.kwargs['id']
        }
        return render(request, 'web/moviesDetail.ejs', context=context)
    
class shows(APIView):
    def get(self, request):
        return render(request, 'web/shows.ejs')
    
class showsDetails(APIView):
    def get(self, request, *args, **kwargs):
        context = {
            'shows' : self.kwargs['id']
        }
        return render(request, 'web/showsDetail.ejs',context=context)
    
class blogs(APIView):
    def get(self, request):
        return render(request, 'web/blog.ejs')
    
class blogDetail(APIView):
    def get(self, request, *args, **kwargs):
        context = {
            'blog' : self.kwargs['id']
        }
        return render(request, 'web/blogDetail.ejs',context=context)    
    
class contact(APIView):
    def get(self, request):
        return render(request, 'web/contact.ejs')

class pricing(APIView):
    def get(self, request):
        return render(request, 'web/pricing.ejs')
    
class myprofile(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "profile": self.kwargs['id']
        }
        return render(request, 'web/myprofile.ejs',context=context)

class viewProfile(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "profile": UserProfile.objects.get(pk=self.kwargs['id'])
        }
        return render(request, 'web/viewprofile.ejs',context=context)
    
class mySettings(APIView):
    def get(self, request):
        return render(request, 'web/myprofile.ejs')
    
class allShows(APIView):
    def get(self, request):
        return render(request, 'web/allShows.ejs')
    
class privacy(APIView):
    def get(self, request):
        return render(request, 'web/privacy.ejs')
    
class terms(APIView):
    def get(self, request):
        return render(request, 'web/terms.ejs')
   
   
###Dashboard Views###
#####################

class adminValidation(APIView):
    def __init__(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))

class dashboard(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        return render(request, 'web/admin/index.ejs') 
    
class userlist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "userprofile": UserProfile.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/userlist.ejs',context=context) 
    
class addlivelink(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            'live':self.kwargs['id'],
            'data': LiveTv.objects.get(pk=1)
        }
        return render(request, 'web/admin/addlive.ejs',context=context) 

class addmoviecategory(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "moviecat": self.kwargs['id']
        }
        return render(request, 'web/admin/addmoviecategory.ejs',context=context)

class moviecategorylist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "cat": MovieCategory.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/moviecatlist.ejs',context=context)  

class addmovie(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            'movie':self.kwargs['id']
        }
        return render(request, 'web/admin/addmovie.ejs',context=context) 
    
class movielist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "movies": Movies.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/movielist.ejs',context=context) 

class addmoviesubcategory(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "showscat": self.kwargs['id']
        }
        return render(request, 'web/admin/addmoviesubcategory.ejs',context=context)

class moviesubcategorylist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "subcat": MovieSubcategory.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/moviesubcategorylist.ejs',context=context) 

class addgenre(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            'genre':self.kwargs['id']
        }
        return render(request, 'web/admin/addgenre.ejs',context=context) 
    
class genrelist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "genres": MovieGenre.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/genrelist.ejs',context=context) 
    
class addproducer(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            'producer':self.kwargs['id']
        }
        return render(request, 'web/admin/addproducer.ejs',context=context) 
    
class producerlist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "producer": MovieProducer.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/producerlist.ejs',context=context) 

class addreels(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            'reels':self.kwargs['id']
        }
        return render(request, 'web/admin/addreels.ejs',context=context) 
    
class reelslist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "reels": MovieReels.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/reelslist.ejs',context=context)  
    
    
class addshowscategory(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "showscat": self.kwargs['id']
        }
        return render(request, 'web/admin/addshowscategory.ejs',context=context) 
    
class showscategorylist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "cat": ShowCategory.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/showscategorylist.ejs',context=context)  

class addshowssubcategory(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "showscat": self.kwargs['id']
        }
        return render(request, 'web/admin/addshowssubcategory.ejs',context=context) 
    
class showssubcategorylist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "subcat": ShowSubCategory.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/showssubcategorylist.ejs',context=context)       

class addshow(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "shows": self.kwargs['id']
        }
        return render(request, 'web/admin/addshow.ejs',context=context)

class showslist(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=UserProfile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('home'))
        context = {
            "shows": Shows.objects.all().order_by('-id')
        }
        return render(request, 'web/admin/showslist.ejs',context=context) 
    
    
###Post Views###
################

class PostProfile(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            profile= UserProfileSerializer(data=request.data)
        else:
            obj = UserProfile.objects.get(pk=self.kwargs['id'])
            profile = UserProfileSerializer(obj,data=request.data)
        if profile.is_valid():
            profile.save()
            return Response(profile.data, status=status.HTTP_201_CREATED)
        return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)

class PostMessage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class postBlog(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
###List Views###
################
class MessagesListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = CompanyPagination
    def get_queryset(self):
        data=Messages.objects.all().order_by('-id')
        return data
    
class BlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    pagination_class = CompanyPagination
    def get_queryset(self):
        data=Blog.objects.all().order_by('-id')
        return data
        
#Api View
class BlogDetailAPIView(APIView):
    def get(self,request,*args,**kwargs):
        blog=Blog.objects.get(pk=self.kwargs['id'])
        ser = BlogSerializer(blog)
        response = {
            'data' : ser.data
        }
        return Response(response) 

#Delete

class DeleteProfile(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=UserProfile.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/userlist')
        except:
            return Response({'result' : False}) 

