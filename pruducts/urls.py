from django.urls import path, include
from django.contrib import admin
from .views import *
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as doc_urls

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("bolims", BolimViewSets)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += doc_urls

