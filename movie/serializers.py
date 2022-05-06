from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from movie.models import *

###Movies###
############
class MoviesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Movies
        fields = '__all__'
        
class MovieCategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = MovieCategory
        fields = '__all__'
        
class MovieSubcategorySerializer(serializers.ModelSerializer):   
    class Meta:
        model = MovieSubcategory
        fields = '__all__'
        
class MovieReelsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MovieReels
        fields = '__all__'
        
class MoviesGenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MovieGenre
        fields = '__all__'

class MovieProducerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MovieProducer
        fields = '__all__'
        