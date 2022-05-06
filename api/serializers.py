from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from api.models import *

        

class LiveSerializer(serializers.ModelSerializer):    
    class Meta:
        model = LiveTv
        fields = '__all__'