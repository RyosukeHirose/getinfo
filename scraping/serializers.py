from rest_framework import serializers
from .models import Scraping
class ScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraping
        fields = '__all__'
