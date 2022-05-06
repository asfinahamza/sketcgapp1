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
from movie.models import *
from movie.serializers import *




class CompanyPagination(pagination.PageNumberPagination):
    page_size = 9
    
###Post Views###
################ 
class PostMoviesSubCategory(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            subCat = MovieSubcategorySerializer(data=request.data)
        else:
            obj = MovieSubcategory.objects.get(pk=self.kwargs['id'])
            subCat = MovieSubcategorySerializer(obj,data=request.data)
        if subCat.is_valid():
            subCat.save()
            return Response(subCat.data, status=status.HTTP_201_CREATED)
        return Response(subCat.errors, status=status.HTTP_400_BAD_REQUEST)

class PostMoviesCategory(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            movieCat = MovieCategorySerializer(data=request.data)
        else:
            obj = MovieCategory.objects.get(pk=self.kwargs['id'])
            movieCat = MovieCategorySerializer(obj,data=request.data)
        if movieCat.is_valid():
            movieCat.save()
            return Response(movieCat.data, status=status.HTTP_201_CREATED)
        return Response(movieCat.errors, status=status.HTTP_400_BAD_REQUEST)

class PostMoviesAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            movies = MoviesSerializer(data=request.data)
        else:
            obj = Movies.objects.get(pk=self.kwargs['id'])
            movies = MoviesSerializer(obj,data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data, status=status.HTTP_201_CREATED)
        return Response(movies.errors, status=status.HTTP_400_BAD_REQUEST)



class addMovieGenre(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            genre= MoviesGenreSerializer(data=request.data)
        else:
            obj = MovieGenre.objects.get(pk=self.kwargs['id'])
            genre = MoviesGenreSerializer(obj,data=request.data)
        if genre.is_valid():
            genre.save()
            return Response(genre.data, status=status.HTTP_201_CREATED)
        return Response(genre.errors, status=status.HTTP_400_BAD_REQUEST)
    
class addMovieProducer(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            producer= MovieProducerSerializer(data=request.data)
        else:
            obj = MovieProducer.objects.get(pk=self.kwargs['id'])
            producer = MovieProducerSerializer(obj,data=request.data)
        if producer.is_valid():
            producer.save()
            return Response(producer.data, status=status.HTTP_201_CREATED)
        return Response(producer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class addMovieReels(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            reels= MovieReelsSerializer(data=request.data)
        else:
            obj = MovieReels.objects.get(pk=self.kwargs['id'])
            reels = MovieReelsSerializer(obj,data=request.data)
        if reels.is_valid():
            reels.save()
            return Response(reels.data, status=status.HTTP_201_CREATED)
        return Response(reels.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
###List View###
###############
class MovieListView(generics.ListAPIView):
    serializer_class = MoviesSerializer
    pagination_class = CompanyPagination
    def get_queryset(self):
        data=Movies.objects.all().order_by('-id')
        return data
    
    
###Category###
##############
class category_js(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        vid=MovieCategory.objects.all()
        video = MovieCategorySerializer(vid,many=True)
        response = {
            'categories' : video.data
        }
        return Response(response)

class subcategory_js(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,id):
        category=MovieCategory.objects.get(pk=id)
        vid=MovieSubcategory.objects.filter(category=category).order_by('title')
        video = MovieSubcategorySerializer(vid,many=True)
        response = {
            'subcategories' : video.data
        }
        return Response(response)
    

###Delete###
############
class deleteMovie(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=Movies.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/MovieListView')
        except:
            return Response({'result' : False})

class deleteMovieCat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=MovieCategory.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/moviecategorylist')
        except:
            return Response({'result' : False})

class deleteMovieSubCat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=MovieSubcategory.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/moviesubcategorylist')
        except:
            return Response({'result' : False})