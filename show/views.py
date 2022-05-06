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
from show.models import *
from show.serializers import *


class CompanyPagination(pagination.PageNumberPagination):
    page_size = 9

###Post Views###
################ 
class addShowsCategory(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            cat= ShowCategorySerializer(data=request.data)
        else:
            obj = ShowCategory.objects.get(pk=self.kwargs['id'])
            cat = ShowCategorySerializer(obj,data=request.data)
        if cat.is_valid():
            cat.save()
            return Response(cat.data, status=status.HTTP_201_CREATED)
        return Response(cat.errors, status=status.HTTP_400_BAD_REQUEST)
    
class addShowsSubCategory(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            subcat= ShowSubCategorySerializer(data=request.data)
        else:
            obj = ShowSubCategory.objects.get(pk=self.kwargs['id'])
            subcat = ShowSubCategorySerializer(obj,data=request.data)
        if subcat.is_valid():
            subcat.save()
            return Response(subcat.data, status=status.HTTP_201_CREATED)
        return Response(subcat.errors, status=status.HTTP_400_BAD_REQUEST)

class addShows(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        if self.kwargs['id'] == 0:
            shows= ShowSerializer(data=request.data)
        else:
            obj = Shows.objects.get(pk=self.kwargs['id'])
            shows = ShowSerializer(obj,data=request.data)
        if shows.is_valid():
            shows.save()
            return Response(shows.data, status=status.HTTP_201_CREATED)
        return Response(shows.errors, status=status.HTTP_400_BAD_REQUEST)
    


###List View###
###############
class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer
    pagination_class = CompanyPagination
    def get_queryset(self):
        data=Shows.objects.all().order_by('-id')
        return data
    
###Category###
##############   
class shows_category_js(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        vid=ShowCategory.objects.all()
        video = ShowCategorySerializer(vid,many=True)
        response = {
            'categories' : video.data
        }
        return Response(response)

class shows_subcategory_js(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,id):
        category=ShowCategory.objects.get(pk=id)
        vid=ShowSubCategory.objects.filter(cat=category).order_by('title')
        video = ShowSubCategorySerializer(vid,many=True)
        response = {
            'subcategories' : video.data
        }
        return Response(response)




###Delete###
############
class deleteShow(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=Shows.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/showslist')
        except:
            return Response({'result' : False})    

class deleteShowsCat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=ShowCategory.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/showscategorylist')
        except:
            return Response({'result' : False}) 

class deleteShowSubCat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        try:
            data=ShowSubCategory.objects.get(pk=self.kwargs['id'])
            data.delete()
            return redirect('/showssubcategorylist')
        except:
            return Response({'result' : False})    