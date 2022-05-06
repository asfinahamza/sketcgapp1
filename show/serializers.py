from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from show.models import *


###Shows###
###########
class ShowCategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = ShowCategory
        fields = '__all__'
        
class ShowSubCategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = ShowSubCategory
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Shows
        fields = '__all__'

class ShowsAPISerializer(serializers.ModelSerializer):   
    class Meta:
        model = Shows
        exclude = ['category']
