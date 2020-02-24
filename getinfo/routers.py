from rest_framework import routers
from scraping.viewsets import ScrapingViewSet, UserViewSet, ArticlesViewSet


router = routers.DefaultRouter()
router.register('scraping', ScrapingViewSet)
router.register('users', UserViewSet)
router.register('articles', ArticlesViewSet)
