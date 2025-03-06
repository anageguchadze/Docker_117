from rest_framework.routers import DefaultRouter
from .views import MuseumViewSet

router = DefaultRouter()

router.register(r'museums', MuseumViewSet, basename='museum')

urlpatterns = router.urls