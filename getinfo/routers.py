from rest_framework import routers
from scraping.viewsets import ScrapingViewSet


router = routers.DefaultRouter()
router.register('scraping', ScrapingViewSet)
