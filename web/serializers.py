from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from web.models import *




class UserProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Messages
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Blog
        fields = '__all__'

        






