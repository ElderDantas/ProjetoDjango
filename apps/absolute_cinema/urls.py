from django.urls import path, include
from rest_framework import routers

from apps.absolute_cinema.api.viewsets import FilmesViewSet

router = routers.DefaultRouter()
router.register(r"filmes", FilmesViewSet, basename="filmes")

urlpatterns = [
    path("", include(router.urls))
]
