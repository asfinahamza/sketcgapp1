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


from api.serializers import *
from api.models import *

class addLiveLink(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, *args, **kwargs):
        obj = LiveTv.objects.get(pk=1)
        live = LiveSerializer(obj,data=request.data)
        if live.is_valid():
            live.save()
            return Response(live.data, status=status.HTTP_201_CREATED)
        return Response(live.errors, status=status.HTTP_400_BAD_REQUEST)