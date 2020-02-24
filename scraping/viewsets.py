from rest_framework import viewsets, filters
from .models import Scraping, User, Article
from .serializers import ScrapingSerializer, UserSerializer, ArticleSerializer


class ScrapingViewSet(viewsets.ModelViewSet):
    queryset = Scraping.objects.all()
    serializer_class = ScrapingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('scraping_id', 'scraping_heading', 'scraping_body')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'username')

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'article')