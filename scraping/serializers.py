from rest_framework import serializers
from .models import Scraping, User, Article

class ScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraping
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
