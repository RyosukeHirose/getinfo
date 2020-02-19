from rest_framework import viewsets, filters
from .models import Scraping
from .serializers import ScrapingSerializer


class ScrapingViewSet(viewsets.ModelViewSet):
    queryset = Scraping.objects.all()
    serializer_class = ScrapingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('scraping_id', 'scraping_heading', 'scraping_body')
