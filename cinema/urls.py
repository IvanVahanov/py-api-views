from django.urls import path, include

from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreAPIView,
    ActorGenericAPIView,
    ActorDetailGenericAPIView,
    CinemaHallViewSet, MovieViewSet)

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailGenericAPIView.as_view(),
         name="actor-detail"),
    path("", include(router.urls)),
]
